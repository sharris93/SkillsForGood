from .common import OpportunitySerializer
from charities.serializers.common import CharitySerializer
from skills.serializers.common import SkillSerializer

class PopulatedOpportunitySerializer(OpportunitySerializer):
    charity = CharitySerializer()
    skills_required = SkillSerializer(many=True)