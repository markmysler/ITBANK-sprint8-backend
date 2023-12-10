# authentication/urls.py

from django.urls import path
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView

from authentication.views import ClienteView, CustomRegisterView



urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("create-client/", ClienteView.as_view(), name="create_client"),
]