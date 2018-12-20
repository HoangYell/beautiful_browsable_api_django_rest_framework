from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from app_story import views


router = routers.DefaultRouter()
router.register(r'story', views.StoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
