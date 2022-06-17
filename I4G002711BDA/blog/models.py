from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField(max_length = 100000)
    Author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    Created_date = models.DateTimeField(max_length=10)
    Published_date = models.DateTimeField(max_length=10)
    
    def __str__(self) -> str:
        return self.Title
    

