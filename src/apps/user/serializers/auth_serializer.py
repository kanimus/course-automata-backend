from rest_framework import serializers
from config.settings.settings import AUTH_USER_MODEL
from apps.user.models import Auth


class UserSerializer(serializers.Serializer):
    google_id = serializers.IntegerField(required=False)
    school_id = serializers.IntegerField(required=False)
    password = serializers.CharField(required=False)
    login = serializers.CharField(required=False)
    user_school_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        user = AUTH_USER_MODEL.objects.create(login=validated_data.get('login'),
                                              user_school_id=validated_data.get('user_school_id'),
                                              school_id=validated_data.get('school_id')
                                              )
        user.set_password(validated_data.get('password'))
        google_id = validated_data.get('google_id', None)
        if google_id:
            auth , created = Auth.objects.get_or_create(google_id=google_id)
            if created:
                auth.user = user
                auth.save()
        return user