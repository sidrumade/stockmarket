from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#
#     # first_name=models.CharField(max_length=15)
#     # last_name=models.CharField(max_length=15)
#     # email=models.CharField(max_length=25)
#     # password=models.CharField(max_length=25)
#
#     def __str__(self):
#         return self.user.username
