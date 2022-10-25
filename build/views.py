from rest_framework import generics, permissions

from .serializers import ComplexSerializer


class ComplexAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ComplexSerializer