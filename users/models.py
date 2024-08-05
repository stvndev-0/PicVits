from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', default='default.jpg')

    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        # Comprueba si la imagen a eliminar no sea la imagen por defecto
        if self.image.name != 'default.jpg':
            self.image.delete(save=False)
            self.image = 'default.jpg'
            self.save()
        super().delete(*args, **kwargs)