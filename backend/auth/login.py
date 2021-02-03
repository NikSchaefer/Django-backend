from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

# pylint: disable=no-member


@api_view(['POST'])
def login_view(request):
    print(request.user, request.session.session_key)
    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(username=username, password=password)

    if user is None:
        return Response("User Doesn't Exist")

    if not request.session or not request.session.session_key:
        request.session.save()
    login(request, user)
    print(request.user, request.session.session_key)

    return Response(request.session.session_key)
