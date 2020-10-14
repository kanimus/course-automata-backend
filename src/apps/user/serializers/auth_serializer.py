from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from apps.user.models import Auth


class AuthSerializer(serializers.Serializer):
    google_id = serializers.IntegerField(required=False)
    school_id = serializers.CharField(required=True)
    login = serializers.CharField(required=True)
    user_school_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        auth = Auth.objects.create(login=validated_data.get('login'),
                                   user_school_id=validated_data.get('user_school_id'),
                                   school_id=validated_data.get('school_id'),
                                   password=make_password(validated_data.get('password')),
                                   )
        auth.save()
        # google_id = validated_data.get('google_id', None)
        # if google_id:
        #     auth, created = Auth.objects.get_or_create(google_id=google_id)
        #     if created:
        #         auth.user = user
        #         auth.save()
        return auth