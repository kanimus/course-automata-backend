import jwt

from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import TokenAuthentication

from apps.user.models import School
from config.user.config import TOKEN_AUTH, SCHOOL_HEADER, JWT_KEY


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):

        User = get_user_model()
        token_cookie = request.COOKIES.get(TOKEN_AUTH)
        school_id = request.headers.get(SCHOOL_HEADER)

        if not token_cookie or not school_id:
            return None
        try:
            # token = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            token = token_cookie.split(' ')[1]
            payload = jwt.decode(
                token, JWT_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token expired.')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing.')

        user = User.objects.filter(id=payload['user_id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is inactive.')

        if school_id not in payload['auth']:
            raise exceptions.AuthenticationFailed('User has not current school.')

        school = School.objects.filter(id=school_id).first()

        if not school:
            raise exceptions.AuthenticationFailed('School not found.')

        user.current_school_id = school.id

        return user, payload['auth']

