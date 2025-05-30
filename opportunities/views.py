from .models import Opportunity
from .serializers import OpportunitySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# This Generic view gives us INDEX and CREATE capabilities
# Allowed methods: GET, POST
# Path: /api/opportunities/
class OpportunityListView(ListCreateAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

# This Generic view gives us SHOW, UPDATE, DELETE capabilities
# Allowed methods: GET, PUT, PATCH, DELETE
# Path: /api/opportunities/:pk/
class OpportunityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer