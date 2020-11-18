from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Posts(models.Model):
    class Meta:
        verbose_name_plural = "posts"

    text=models.TextField()
    upvote=models.IntegerField()
    date = models.DateTimeField(default=timezone.now, blank=False)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    ip=models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.text

class Comment(models.Model):
    class Meta:
        verbose_name_plural="comments"
    ctext=models.TextField()
    upvote=models.IntegerField()
    downvote=models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post=models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, blank=False)
    def __str__(self):
        return self.ctext
