from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class UserListView(APIView):
    def get(self, request, format=None):
        emails = [user.email for user in User.objects.all()]
        return Response(emails)
