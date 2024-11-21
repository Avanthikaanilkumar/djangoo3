from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    
    class Meta:
        permissions=[
            ("can_view_protected_page","can view protected page"),
        ]
class user1(models.Model):
    user_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class new_model(models.Model):
    id=models.IntegerField(primary_key=True)
    new_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


