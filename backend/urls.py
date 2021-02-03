from django.urls import path

from .auth.create import create_user_view
from .auth.login import login_view

urlpatterns = [
    path("create", create_user_view),
    path("login", login_view),
]
