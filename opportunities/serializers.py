from .models import Opportunity
from rest_framework import serializers
from skills.serializers import SkillSerializer

# Base serializer
class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'


# Populated serializer
#   - populate the skills_required field
class PopulatedOpportunitySerializer(OpportunitySerializer):
    skills_required = SkillSerializer(many=True)