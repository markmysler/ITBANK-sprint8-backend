from django.urls import path
from .views import TarjetaListView

urlpatterns = [
   path('tarjeta/<int:customer_id>/', TarjetaListView.as_view()),
]
