from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utils.permissions import IsOwnerOrReadOnly
from .models import Charity
from django.shortcuts import get_object_or_404

#  Serializers
from .serializers.common import CharitySerializer
from .serializers.populated import PopulatedCharitySerializer

# Path associated with this class: /api/charities/
# Methods accepted: GET, POST
class CharityListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Index
    def get(self, request):
        charities = Charity.objects.all()
        serialized_charities = CharitySerializer(charities, many=True)
        return Response(serialized_charities.data)

    # Create
    def post(self, request):
        request.data['owner'] = request.user.id # This line takes the authenticated user's id and provides it as the owner on the request body
        serialized_charity = CharitySerializer(data=request.data)
        serialized_charity.is_valid(raise_exception=True)
        serialized_charity.save()
        return Response(serialized_charity.data, 201)



# Path associated with this class: /api/charities/:pk/
# Methods accepted: GET, PUT, DELETE
class CharityDetailView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    # Show
    def get(self, request, pk):
        charity = get_object_or_404(Charity, pk=pk)
        serialized_charity = PopulatedCharitySerializer(charity)
        return Response(serialized_charity.data)

    # Update
    def put(self, request, pk):
        charity = get_object_or_404(Charity, pk=pk)
        
        # Once charity object is found, check ownership, raising PermissionDenied if we don't get a match
        self.check_object_permissions(request, charity)
        
        serialized_charity = CharitySerializer(charity, data=request.data, partial=True)
        serialized_charity.is_valid(raise_exception=True)
        serialized_charity.save()
        return Response(serialized_charity.data)

    # Delete
    def delete(self, request, pk):
        charity = get_object_or_404(Charity, pk=pk)

        # Once charity object is found, check ownership, raising PermissionDenied if we don't get a match
        self.check_object_permissions(request, charity)
        
        charity.delete()
        return Response(status=204)