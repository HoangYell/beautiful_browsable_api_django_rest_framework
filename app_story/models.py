from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField(blank=True)
    feeling = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    music = models.URLField(blank=True)
    image = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('datetime',)