from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'{self.title} ~ {self.author.username}'
