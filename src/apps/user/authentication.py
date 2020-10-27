import jwt
from rest_framework.authentication import TokenAuthentication
from config.user.config import TOKEN_AUTH
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model

from apps.user.models import School


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):

        User = get_user_model()
        token_cookie = request.COOKIES.get(TOKEN_AUTH)
        school_id = request.headers.get('SCHOOL')

        if not token_cookie or not school_id:
            return None
        try:
            # token = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            token = token_cookie.split(' ')[1]
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token expired.')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing.')

        user = User.objects.filter(id=payload['user_id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is inactive.')

        school = School.objects.filter(id=school_id).first()

        if not school:
            raise exceptions.AuthenticationFailed('School not found.')

        user.current_school_id = school.id

        return user, payload['auth']


class TokenAuthSupportCookie(TokenAuthentication):
    """
    Extend the TokenAuthentication class to support cookie based authentication
    """
    def authenticate(self, request):
        # Check if 'token' is in the request cookies.
        # Give precedence to 'Authorization' header.
        if TOKEN_AUTH in request.COOKIES and \
                        'HTTP_AUTHORIZATION' not in request.META:
            return self.authenticate_credentials(
                request.COOKIES.get(TOKEN_AUTH)
            )
        return super().authenticate(request)