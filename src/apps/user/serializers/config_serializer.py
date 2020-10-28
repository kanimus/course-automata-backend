from rest_framework import serializers

from apps.user.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'short_name', 'name_nationalized', 'short_name_nationalized')
