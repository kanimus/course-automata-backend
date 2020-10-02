from rest_framework.exceptions import NotFound
from apps.user.serializers import auth_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.models import Auth, User
from apps.user.serializers import UserSerializer
from apps.user.helpers.auth_helpers import is_user_exist
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class LogoutView():
    pass


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user, school = is_user_exist(serializer.validated_data['login'],
                                         serializer.validated_data['user_school_id'],
                                         serializer.validated_data['school_id']
                                         )
            if not school:  # Error School is not exist
                raise NotFound('School is not found.', code='school_not_found')
            elif not user:  # User is not exist but school exist. Create new user and token for him.
                user = serializer.save()
                token = Token.objects.Create(user=user)
                return Response({
                    'token': token
                })
            else:  # User has been existed. Update token.
                token = Token.objects.get(user=user)
                token.delete()
                token = Token.objects.Create(user=user)
                return Response({
                    'token': token
                })
