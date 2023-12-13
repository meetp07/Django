from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    # will set current time, if you want to set a time when post was created then auto_now_add=True, you will not be able to change the time.
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    #will delete the post if author is deleted, but doesn't delete the author if post is deleted.

    def __str__(self):
        return self.title