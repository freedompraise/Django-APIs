from rest_framework import generics # used for DRY 
# It infers the response, and enables the views to be taken directly from the model class or seriaizer class

from .models import *
from .serializers import * 

class PollList(generics.ListCreateAPIView):  
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
        
        