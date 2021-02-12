from django.urls import path

from .auth.create import create_user_view
from .auth.login import login_view
from .auth.logout import logout_view

urlpatterns = [
    # Auth
    path("create", create_user_view),
    path("login", login_view),
    path("logout", logout_view),

]
