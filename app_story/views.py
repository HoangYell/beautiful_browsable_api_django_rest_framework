from rest_framework import viewsets
from rest_framework import permissions
from app_story.models import Story
from app_story.serializers import StorySerializer


class StoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Story.objects.all()
    serializer_class = StorySerializer
