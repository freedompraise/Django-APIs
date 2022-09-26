from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView

from .models import Poll
from .serializers import * 

def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {
        "results":list(polls.values(
            "question","created_by__username","pub_date"
            ))
        }
    return JsonResponse(data)

def polls_detail(request,pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "results":{
            "question":poll.question,
            "created_by":poll.created_by.username,
            "pub_date":poll.pub_date
        }
    }
    # TO create an polls object with serializers : 
    # poll_serializer = PollSerializer(data={"question": "Rice or Beans", "created_ : by": 1})

    return JsonResponse(data)
