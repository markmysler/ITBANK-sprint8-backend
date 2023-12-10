from django.urls import path
from .views import CuentaListView

urlpatterns = [
   path('cuenta/<int:customer_id>/', CuentaListView.as_view()),
]
