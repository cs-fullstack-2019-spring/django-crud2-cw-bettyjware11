from django.db import models


# Data model for User
class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, unique=True)
    phone_number = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name
