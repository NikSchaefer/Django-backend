from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

# pylint: disable=no-member


@api_view(['POST'])
def login_view(request):

    username = request.data["username"]
    password = request.data["password"]

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({
            "status": "No",
            "detail": "Invalid Credidentals"
        })

    login(request, user)

    return Response({
        "status": "Ok",
        "sessionid": request.session.session_key,
        "detail": "Logged In"
    })
