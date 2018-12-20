from rest_framework import serializers
from app_story.models import Story


class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'text', 'feeling', 'solution', 'music', 'image', 'user', 'datetime')