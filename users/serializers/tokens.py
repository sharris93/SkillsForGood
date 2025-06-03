from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Customise the payload (claims)
        token['user'] = {
            'id': user.id,
            'username': user.username,
            'location': user.location
        }

        # Return the modified token
        return token