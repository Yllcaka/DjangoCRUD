from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User #Qikjo eshte per Usera

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postDetail', kwargs={'pk':self.pk})    
        