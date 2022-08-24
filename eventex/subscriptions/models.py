from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=155)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)