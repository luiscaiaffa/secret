from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class ListUsers(APIView):

    def get(self, request, format=None):

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)