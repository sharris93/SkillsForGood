from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Charity
from .serializers import CharitySerializer
from django.shortcuts import get_object_or_404

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
        serialized_charity = CharitySerializer(data=request.data)
        serialized_charity.is_valid(raise_exception=True)
        serialized_charity.save()
        return Response(serialized_charity.data, 201)



# Path associated with this class: /api/charities/:pk/
# Methods accepted: GET, PUT, DELETE
class CharityDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Show
    def get(self, request, pk):
        charity = get_object_or_404(Charity, pk=pk)
        serialized_charity = CharitySerializer(charity)
        return Response(serialized_charity.data)

    # Update
    def put(self, request, pk):
        charity = get_object_or_404(Charity, pk=pk)
        serialized_charity = CharitySerializer(charity, data=request.data, partial=True)
        serialized_charity.is_valid(raise_exception=True)
        serialized_charity.save()
        return Response(serialized_charity.data)

    # Delete
    def delete(self, request, pk):
        charity = get_object_or_404(Charity, pk=pk)
        charity.delete()
        return Response(status=204)