from rest_framework.authentication import TokenAuthentication
from config.user.config import TOKEN_AUTH


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