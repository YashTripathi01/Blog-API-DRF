from rest_framework import serializers

from authentication import models


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = models.User
        fields = ['email', 'name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError(
                'Password and Confirm Password does not match')

        return attrs

    def create(self, validated_data):
        return models.User.objects.create_user(**validated_data)


class UserListSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.User
        fields = ['id', 'email', 'posts', 'comments']


# class UserLoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(max_length=255)

#     class Meta:
#         model = models.User
#         fields = ['email', 'password']
