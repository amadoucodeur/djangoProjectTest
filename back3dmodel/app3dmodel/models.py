
from django.db import models
from django.contrib.auth.models import User

class Model3d(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='model_images/')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    badge = models.ManyToManyField(Badge, blank=True)

# Create your models here.
