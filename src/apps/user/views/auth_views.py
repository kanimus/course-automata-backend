from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.helpers.auth_helpers import is_auth_data_exist
from apps.user.models import Auth
from apps.user.serializers import UserSerializer
from config.user.config import TOKEN_AUTH, SECURE_COOKIE


class LogoutView(APIView):
    @swagger_auto_schema(responses={200: "Logout"})
    def get(self, request, format=None):
        # simply delete the token to force a login
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie(key=TOKEN_AUTH)
        return response


class LoginView(ObtainAuthToken):

    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserSerializer, responses={201: "OK"}, security=[])
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user, school, auth = is_auth_data_exist(serializer.validated_data['login'],
                                                    serializer.validated_data['user_school_id'],
                                                    serializer.validated_data['school_id']
                                                    )
            if not school:  # Error School is not exist
                raise NotFound('School is not found.', code='school_not_found')
            elif not user and auth:  # User is not exist but auth exist. Create new user and token for him.
                user = serializer.save()
                auth.user = user
                auth.save()
            elif not user and not auth:
                user = serializer.save()
                Auth.objects.create(user=user, google_id=serializer.validated_data.get('school_id', None))
            else:  # User and auth have been existed. Update token for current user.
                token = Token.objects.get(user=user)
                token.delete()
            token = Token.objects.create(user=user)
            response = Response()
            response.set_cookie(key=TOKEN_AUTH, value=token, httponly=True, secure=SECURE_COOKIE)  # TODO: for prod need use secure=True
            return response
