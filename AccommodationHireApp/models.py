from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
class BaseModel(models.Model):
    update_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Role(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class User(AbstractUser, BaseModel):
    role = models.ForeignKey(Role, related_name='user',on_delete=models.CASCADE,null=True)
    avatar_user = CloudinaryField('image')
class Post(BaseModel):
    pass


