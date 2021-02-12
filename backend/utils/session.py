from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
# pylint: disable=no-member

def user_from_session(session_key):
    try:
        session = Session.objects.get(pk=session_key)
    except:
        return {
            "status": "No",
            "detail": "No Session Found"
        }
    decoded = session.get_decoded()
    user_id = decoded.get("_auth_user_id")
    user = User.objects.get(pk=user_id)
    return user
