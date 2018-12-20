from app_user import views
from django.urls import path
from rest_framework import routers
from django.conf.urls import include


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]