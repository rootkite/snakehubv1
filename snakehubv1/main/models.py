from django.db import models

# Create your models here.

#model for newsletter users

class NewsLetterUser(models.Model):
    name = models.CharField(max_length=50)
    phone_number= models.CharField(max_length=11)
    email = models.EmailField(unique=True)


    