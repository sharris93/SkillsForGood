from rest_framework import serializers
from ..models import Charity

# * Base Serializer
class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = '__all__'