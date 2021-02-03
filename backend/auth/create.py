
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..utils.exists import username_exists 
# pylint: disable=no-member

@api_view(['POST'])
def create_user_view(request):
    username = str(request.data["username"])
    password = str(request.data["password"])

    if username_exists(username):
        return Response("User Exists")
    if len(list(username)) < 6:
        return Response("Requires Longer Username")
    if len(list(password)) < 6:
        return Response("Requires Longer Password")

    user = User.objects.create_user(
        username=username, email="test@gmail.com", password=password)

    login(request, user)
    return Response("User Created")

