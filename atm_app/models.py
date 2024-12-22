from django.db import models
class User(models.Model):
    acc_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    adhaar_no = models.IntegerField(unique=True)
    mobile = models.IntegerField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    pin = models.IntegerField(max_length=4)
    def __str__(self):
        return f"{self.name} ({self.acc_no})"
# Create your models here.
