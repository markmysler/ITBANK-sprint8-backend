from django.urls import path
from .views import SucursalListView

urlpatterns = [
   path('sucursal/', SucursalListView.as_view()),
]
