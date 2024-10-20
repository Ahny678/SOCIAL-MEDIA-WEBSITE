from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class VideoPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='post_videos/')
    thumbnail = models.FileField(upload_to='video_thumbnails/')
    description = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Post" 
    
    def get_absolute_url(self):
        return reverse('mv', kwargs={'pk' : self.pk})
    

