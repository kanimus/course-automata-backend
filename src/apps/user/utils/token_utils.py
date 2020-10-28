import datetime
import jwt

from config.user import config


def _generate_token(user, auths):
    token_payload = {
        'user_id': user.id,
        'auth': auths,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=config.JWT_EXPIRATION_TIME),
        # TODO: needs set it by config
        'iat': datetime.datetime.utcnow(),
    }
    token = jwt.encode(token_payload, config.JWT_KEY, algorithm='HS256').decode('utf-8')
    return token


def generate_token(user, auths=None, auth=None):
    if auths is not list:
        auths = []
    if auth:
        if auth not in auths:
            auths.append(auth)
    return _generate_token(user, auths)


def delete_token(user, auths, auth):
    auths.remove(auth)
    return _generate_token(user, auths)


def prepare_token(token):
    return 'Token ' + token


def set_cookie_token(response, token):
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=config.COOKIE_EXPIRATION_TIME),
        "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key=config.TOKEN_AUTH, value=prepare_token(token),
                        httponly=True, secure=config.SECURE_COOKIE, max_age=config.COOKIE_EXPIRATION_TIME,
                        expires=expires)
