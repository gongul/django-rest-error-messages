
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    