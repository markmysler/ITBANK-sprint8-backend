from django.urls import path
from .views import PrestamoView

urlpatterns = [
  path('prestamo/<int:customer_id>/', PrestamoView.as_view(), name='prestamo'),
]
