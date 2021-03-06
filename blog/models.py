from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    text_preview = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    list_image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='images/', blank=True, null=True)
    medium_post = models.BooleanField(default=False)
    medium_url = models.URLField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
