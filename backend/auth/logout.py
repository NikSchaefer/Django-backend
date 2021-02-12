from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session

# pylint: disable=no-member


@api_view(['POST'])
def logout_view(request):
    session_key = request.data["session"]
    session = Session.objects.filter(session_key=session_key)
    
    session.delete()

    logout(request)

    return Response({
        "status": "Ok",
    })
