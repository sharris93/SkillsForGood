from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Charity # Import the model
from .serializers import CharitySerializer
from django.shortcuts import get_object_or_404 # method that finds a single object or raises a 404 exception

# Path associated with this class: /api/charities
# Methods accepted: GET, POST
class CharityListView(APIView):
    # Index
    def get(self, request):
        charities = Charity.objects.all() # all() returns all objects in the table related to the model used
        serialized_charities = CharitySerializer(charities, many=True)
        return Response(serialized_charities.data)

    # Create
    def post(self, request):
        # When we want to deserialize (create or update an object) we pass the data through on the data key of the serializer
        serialized_charity = CharitySerializer(data=request.data)
        # Next, we check whether the data passed in the body of the request is valid
        # It will check this data against the model
        # This will return a boolean, true if the data is valid, false if not
        serialized_charity.is_valid(raise_exception=True)
        # If the data is valid, we save it
        serialized_charity.save()
        # Finally we send back the created object
        return Response(serialized_charity.data, 201)



# Path associated with this class: /api/charities/:pk
# Methods accepted: GET, PUT, DELETE
class CharityDetailView(APIView):
    # Show
    def get(self, request, pk):
        charity = get_object_or_404(Charity, pk=pk)
        serialized_charity = CharitySerializer(charity)
        return Response(serialized_charity.data)
    
        # try:
        #     charity = Charity.objects.get(pk=pk)
        #     serialized_charity = CharitySerializer(charity)
        #     return Response(serialized_charity.data)
        # except Charity.DoesNotExist as e:
        #     print('Not Found')
        #     return Response({ 'detail': 'Charity not found' }, 404)
        # except:
        #     print('An error occurred')
        #     return Response('Something went wrong', 500)


    # Update
    def put(self, request, pk):
        charity = get_object_or_404(Charity, pk=pk) # Find the existing charity in the DB
        serialized_charity = CharitySerializer(charity, data=request.data, partial=True) # Pass the existing instance into the serializer with the request.data
        serialized_charity.is_valid(raise_exception=True) # We validate request.data
        serialized_charity.save() # If valid, we save the changes to the database
        return Response(serialized_charity.data) # Send a response to the client

    # Delete
    def delete(self, request, pk):
        charity = get_object_or_404(Charity, pk=pk)
        charity.delete()
        return Response(status=204)