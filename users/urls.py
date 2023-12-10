from django.urls import path
from .views import UserView

urlpatterns = [
    path('user/', UserView.as_view()),
    # Add other paths as needed
]
