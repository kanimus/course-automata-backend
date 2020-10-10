from rest_framework import serializers

from apps.user.models import User


class UserSerializer(serializers.Serializer):
    google_id = serializers.IntegerField(required=False)
    school_id = serializers.IntegerField(required=True)
    login = serializers.CharField(required=True)
    user_school_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        user = User.objects.create(login=validated_data.get('login'),
                                   user_school_id=validated_data.get('user_school_id'),
                                   school_id=validated_data.get('school_id')
                                   )
        user.set_password(validated_data.get('password'))
        user.save()
        # google_id = validated_data.get('google_id', None)
        # if google_id:
        #     auth, created = Auth.objects.get_or_create(google_id=google_id)
        #     if created:
        #         auth.user = user
        #         auth.save()
        return user