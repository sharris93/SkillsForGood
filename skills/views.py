from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from utils.permissions import IsAdminOrReadOnly
from .models import Skill
from .serializers.common import SkillSerializer

# List view
class SkillListView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminOrReadOnly]

# Detail view
class SkillDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminOrReadOnly]