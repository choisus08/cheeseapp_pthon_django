from .models import Cheese
from rest_framework import viewsets, permissions
from .serializers import CheeseSerializer

# Create your views here.

class CheeseViewSet(viewsets.ModelViewSet):
    # main query for the index route
    queryset = Cheese.objects.all()
    # serializer class for serializing output
    serializer_class = CheeseSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny]