from .common import CharitySerializer
from users.serializers.common import UsernameSerializer
from opportunities.serializers.common import OpportunityTitleSerializer

class PopulatedCharitySerializer(CharitySerializer):
    owner = UsernameSerializer()
    opportunities = OpportunityTitleSerializer(many=True)