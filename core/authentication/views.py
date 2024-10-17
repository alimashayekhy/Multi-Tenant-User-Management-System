# authentication/views.py

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CustomTokenObtainPairSerializer, LogoutSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to obtain JWT tokens with additional user information.
    """
    serializer_class = CustomTokenObtainPairSerializer


class LogoutView(generics.GenericAPIView):
    """
    View to handle user logout by blacklisting the refresh token.
    """
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)