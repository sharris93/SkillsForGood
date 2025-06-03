from ..models import Opportunity
from rest_framework import serializers

# Base serializer
class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'


class OpportunityTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ['id', 'title']