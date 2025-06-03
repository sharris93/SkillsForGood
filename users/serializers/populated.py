from rest_framework.serializers import ModelSerializer
from ..models import User
from skills.serializers.common import SkillSerializer
from charities.serializers.common import CharitySerializer

class ProfileSerializer(ModelSerializer):
    skills = SkillSerializer(many=True)
    charities = CharitySerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'location', 'is_staff', 'skills', 'charities']