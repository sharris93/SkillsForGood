from .models import Opportunity
from .serializers.common import OpportunitySerializer
from .serializers.populated import PopulatedOpportunitySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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

    # This method replaces serializer_class attribute
    # Inside, we need to return a serializer class to be used
    # The method allows us to select the serializer class dynamically rather that setting it statically
    def get_serializer_class(self):
        # If the request has a method of GET, we want to use the populated serializer to display the charity as an object
        if self.request.method == 'GET':
            return PopulatedOpportunitySerializer
        
        # If the request is anything other than a GET, we want to use the common serializer, with the int representation of the charity
        return OpportunitySerializer