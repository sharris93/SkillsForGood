from charities.models import Charity
from charities.serializers import CharitySerializer
from rest_framework.response import Response

class ListCreateAPIView():
    def __init__(self):
        pass

    def get(self, request):
        charities = self.queryset # all() returns all objects in the table related to the model used
        serialized_charities = self.serializer(charities, many=True)
        return Response(serialized_charities.data)

    def post(self, request):
        pass


class MyNewView(ListCreateAPIView):
    queryset = Charity.objects.all()
    serializer = CharitySerializer()