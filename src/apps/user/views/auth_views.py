from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.models import User
from apps.user.serializers import AuthSerializer
from apps.user.utils.auth_utils import is_auth_data_exist
from apps.user.utils.token_utils import generate_token, delete_token, set_cookie_token, prepare_token
from config.user import config

config_settings_params = openapi.Parameter('school_id', openapi.IN_BODY, description="school id from urls pattern",
                                           type=openapi.TYPE_INTEGER)


class LogoutView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'school_id': openapi.Schema(type=openapi.FORMAT_UUID, description='school_id'),
        }
    ), responses={200: "Logout"})
    def post(self, request, format=None):
        # simply delete the token to force a login
        user = request.user
        token = delete_token(user, request.auth, user.current_school_id)
        response = Response(status=status.HTTP_200_OK)
        set_cookie_token(response, token)
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
                auth = serializer.save(user=user)
                token = generate_token(user, request.auth, auth.school_id)
            elif not user and not auth:
                user = User.objects.create(google_id=serializer.validated_data.get('school_id', None))
                auth = serializer.save(user=user)
                token = generate_token(user, request.auth, auth=auth.school_id)
            else:  # User and auth have been existed. Update token for current user.
                token = generate_token(user, request.auth, auth=auth.school_id)
            response = Response()
            # response.set_cookie(key=config.TOKEN_AUTH, value=prepare_token(token),
            #                     httponly=True,
            #                     )
            set_cookie_token(response, token)
            return response
