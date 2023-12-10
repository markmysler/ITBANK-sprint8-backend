from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
urlpatterns = [
    path('', include(router.urls))
]
