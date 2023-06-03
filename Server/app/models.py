from django.db import models


class ClientManager(models.Manager):
    def create_client(self, name, email, PhoneNumber):
        client = self.create(name=name, email=email, PhoneNumber=PhoneNumber)
        # Additional custom logic if needed
        return client


# Create your models here.
class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

class Client(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=30, default="")
    PhoneNumber = models.CharField(max_length=10,default="")

    def __str__(self):
        return self.email





