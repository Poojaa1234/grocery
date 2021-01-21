from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('PENDING','pending'),
    ('BOUGHT', 'bought'),
    ('NOT AVAILABLE','not available'),
)

class Grocery(models.Model):
    name = models.TextField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES,default='PENDING',max_length=20)
    date = models.DateField()



