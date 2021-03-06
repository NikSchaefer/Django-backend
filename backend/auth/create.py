
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..utils.exists import username_exists 
# pylint: disable=no-member
from ..utils.validate import validate
import re
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
@api_view(['POST'])
def create_user_view(request):
    try:
        username = request.data["username"]
        password = request.data["password"]
    except:
        return Response({
            "status": "No",
            "detail": "Incorrect Fields Provided",
        })
    if not EMAIL_REGEX.match(username):
        return Response({
            "status": "No",
            "detail": "Invalid Email Configuration"
        })

    if username_exists(username):
        return Response({
            "status": "No",
            "detail": "This Email Already has an Account"
        })
    if len(list(username)) < 6:
        return Response({
            "status": "No",
            "detail": "Use a longer username"
        })
    validation = validate(password)
    if validation != "Good":
        return Response({
            "status": "No",
            "detail": validation
        })
    user = User.objects.create_user(
        username=username, email=username, password=password)

    login(request, user)
    return Response({
        "status": "Ok",
        "sessionid": request.session.session_key,
    })

