from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

# pylint: disable=no-member


@api_view(['POST'])
def login_view(request):
    logout(request)

    return Response("Logged Out")
