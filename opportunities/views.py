from .models import Opportunity
from .serializers.common import OpportunitySerializer
from .serializers.populated import PopulatedOpportunitySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# This Generic view gives us INDEX and CREATE capabilities
# Allowed methods: GET, POST
# Path: /api/opportunities/
class OpportunityListView(ListCreateAPIView):
    queryset = Opportunity.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedOpportunitySerializer
        return OpportunitySerializer

# This Generic view gives us SHOW, UPDATE, DELETE capabilities
# Allowed methods: GET, PUT, PATCH, DELETE
# Path: /api/opportunities/:pk/
class OpportunityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Opportunity.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedOpportunitySerializer
        return OpportunitySerializer
    

# This view will give us tailored opportunities for authenticated users
# Method allowed: GET
# Path: /api/opportunities/matched/
class OpportunityMatchedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 1. Get the signed in user's skills list
        skills_list = request.user.skills.all()
        # 2. Query the opportunity model, ensuring we filter the results based on the skills_required field
        #   - We will filter by using `skills_required__in=[1, 2, 3]`
        #   - We will then use distinct() to eliminate duplicates from the results
        opportunities = Opportunity.objects.filter(skills_required__in=skills_list).distinct()
        # 3. Serialize the data to be returned
        serialized_opportunities = OpportunitySerializer(opportunities, many=True)
        # 4. return response to the client
        return Response(serialized_opportunities.data)