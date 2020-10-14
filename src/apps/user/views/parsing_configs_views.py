from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.exceptions import ServerError
from apps.user.helpers.config_helper import get_patterns_or_none, get_school_config_or_none
from apps.user.models import School
from apps.user.serializers import SchoolSerializer

config_settings_params = openapi.Parameter('school_id', openapi.IN_QUERY, description="school id from urls pattern", type=openapi.TYPE_INTEGER)


class UserPatternsView(APIView):

    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: "Json data"}, security=[])
    def get(self, request, format=None):
        data = get_patterns_or_none()
        if not data:
            raise ServerError()
        return Response(data=data)


class ConfigSettingsView(APIView):

    permission_classes = [AllowAny]

    @swagger_auto_schema(manual_parameters=[config_settings_params], responses={200: "Json data"}, security=[])
    def get(self, request, format=None):
        school_id = request.query_params.get('school_id')
        if not school_id:
            raise NotFound()
        school_config = get_school_config_or_none(school_id)
        if not school_config:
            raise NotFound()
        return Response(data=school_config)


class GetSchoolDataView(APIView):

    permission_classes = [AllowAny]

    @swagger_auto_schema(manual_parameters=[config_settings_params], responses={200: SchoolSerializer}, security=[])
    def get(self, request, format=None):
        school_id = request.query_params.get('school_id')
        if not school_id:
            raise NotFound()
        school_data = School.objects.filter(id=school_id).first()
        if not school_data:
            raise NotFound()
        response = SchoolSerializer(school_data)
        return Response(data=response.data)
