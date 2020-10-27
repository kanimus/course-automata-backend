# accounts.utils
import datetime
import jwt
from config.user.config import JWT_KEY, JWT_EXPIRATION_TIME


def _generate_token(user, auths):
    token_payload = {
        'user_id': user.id,
        'auth': auths,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=JWT_EXPIRATION_TIME),  # TODO: needs set it by config
        'iat': datetime.datetime.utcnow(),
    }
    token = jwt.encode(token_payload, JWT_KEY, algorithm='HS256').decode('utf-8')
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
