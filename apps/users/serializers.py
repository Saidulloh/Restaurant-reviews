from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'created_at',
            'password',
        )

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
