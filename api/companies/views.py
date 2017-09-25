from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team
from .serializers import TeamSerializer

class Teamlist(APIView):

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# Create your views here.
