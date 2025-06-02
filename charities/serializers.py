from rest_framework import serializers
from .models import Charity
from users.serializers import UsernameSerializer

# * Base Serializer
class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = '__all__'



# * Populated Serializer
class PopulatedCharitySerializer(CharitySerializer):
    owner = UsernameSerializer()