from django.db import models

# Create your models here.

class User(models.Model):
    Email = models.EmailField(max_length = 30)

    def __str__(self):
        return self.Email
