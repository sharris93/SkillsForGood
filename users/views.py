from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers.common import UserSerializer
from .serializers.populated import ProfileSerializer

# Methods allowed: POST
# Path: /api/auth/sign-up/
class SignUpView(APIView):
    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response({ f'detail': 'Sign up successful.' })
    

# Profile view
# Methods accepted: GET
# Path: /api/auth/profile
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = ProfileSerializer(request.user)
        return Response(profile.data)