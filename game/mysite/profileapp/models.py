from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    
    def get_absolute_url(self):
        return reverse('profile')