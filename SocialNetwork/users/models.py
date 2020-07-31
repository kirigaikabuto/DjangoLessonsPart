from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    about = models.TextField()
    photo = models.FileField(upload_to="user_photos/")
    city = models.CharField(max_length=255)
    hobby = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username