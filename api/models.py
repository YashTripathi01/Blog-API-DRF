# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('authentication.User',
                              related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    body = models.TextField(blank=False)
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(
        'authentication.User', related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
