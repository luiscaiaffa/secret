from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

import requests


class BaseA(APIView):

    def get(self, request, *args, **kwargs):
        cpf = self.kwargs['cpf']
        url = f'http://secret_web_1:8001/{cpf}/'
        r = requests.get(url)
        return Response(r.json(), r.status_code)


class BaseB(APIView):

    def get(self, request, *args, **kwargs):
        cpf = self.kwargs['cpf']
        url = f'http://secret_web2_1:8002/{cpf}/'
        r = requests.get(url)
        return Response(r.json(), r.status_code)


class BaseC(APIView):

    def get(self, request, *args, **kwargs):
        cpf = self.kwargs['cpf']
        url = f'http://secret_web3_1:8003/{cpf}/'
        r = requests.get(url)
        return Response(r.json(), r.status_code)