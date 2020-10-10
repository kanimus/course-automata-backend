from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR


class ServerError(APIException):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('Internal server error.')
    default_code = 'server_error'
