from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.helpers.auth_helpers import is_auth_data_exist
from apps.user.models import User
from apps.user.serializers import AuthSerializer
from config.user.config import TOKEN_AUTH, SECURE_COOKIE

config_settings_params = openapi.Parameter('school_id', openapi.IN_BODY, description="school id from urls pattern", type=openapi.TYPE_INTEGER)


class LogoutView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'school_id': openapi.Schema(type=openapi.FORMAT_UUID, description='school_id'),
        }
    ), responses={200: "Logout"})
    def post(self, request, format=None):
        # simply delete the token to force a login
        school_id = request.data.get('school_id', None)
        if not school_id:
            raise NotFound()
        user = request.user
        auth = user.auth_set.filter(school_id=school_id).first()
        if not auth:
            raise NotFound()
        auth.isAuthenticated = False
        auth.save()
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie(key=TOKEN_AUTH)
        return response


class LoginView(ObtainAuthToken):

    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=AuthSerializer, responses={201: "OK"}, security=[])
    def post(self, request, *args, **kwargs):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user, school, auth = is_auth_data_exist(serializer.validated_data['login'],
                                                    serializer.validated_data['user_school_id'],
                                                    serializer.validated_data['school_id']
                                                    )
            if not school:  # Error School is not exist
                raise NotFound('School is not found.', code='school_not_found')
            elif not auth and user:  # Auth is not exist but user exist. Create new auth.
                auth = serializer.save()
                auth.user = user
                auth.save()
                token = Token.objects.get(user=user)
            elif not user and not auth:
                auth = serializer.save()
                user = User.objects.create(google_id=serializer.validated_data.get('school_id', None))
                auth.user = user
                auth.save()
                token = Token.objects.create(user=user)
            else:  # User and auth have been existed. Update token for current user.
                token = Token.objects.get(user=user)
            response = Response()
            response.set_cookie(key=TOKEN_AUTH, value=token, httponly=True, secure=SECURE_COOKIE)  # TODO: for prod need use secure=True
            return response
