from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
class table(models.Model):
    email= models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    age= models.IntegerField()

class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Hashed password

    def save(self, *args, **kwargs):
        if not self.pk:  # Ensure password is hashed only on initial save
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.username