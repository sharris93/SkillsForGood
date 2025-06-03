from rest_framework import serializers
from ..models import User
from django.contrib.auth import password_validation


# This serializer is used for authentication
class UserSerializer(serializers.ModelSerializer):
    # Define fields as write only
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'password_confirmation', 'location']

    def validate(self, data):
        # Check if the passwords match, raise a ValidationError if they do not
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({ 'password': 'Passwords do not match' })
        
        # Omit this line if you want weak password validation
        password_validation.validate_password(data['password'])
        
        return data # Always return the validated data after doing your checks

    def create(self, validated_data):
        validated_data.pop('password_confirmation') # Remove password confirmation to prevent an error with unexpected field
        return User.objects.create_user(**validated_data)
    

# This serializer will be used when populating the owner on a charity
class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']