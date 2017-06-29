from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from MyTeam.models import TeamMember
from MyTeam.serializer import TeamMemberSerializer
from rest_framework import mixins
from rest_framework import generics


def index(request):
    return HttpResponse("Hello, world. You're at the MyTeam index.")

class TeamMemberList(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
