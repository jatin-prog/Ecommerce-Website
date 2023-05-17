from django.db import models

# Create your models here.

'''class message(models.Model):
    mid=models.AutoField(primary_key=True)
    text=models.TextField()
    time=models.TextField()
    sender=models.TextField()'''




class item(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField()
    price=models.FloatField()
    discription=models.TextField()
    img=models.TextField()

class cartitem(models.Model):
    itemid=models.TextField()
    name=models.TextField()
    price=models.TextField()
    img=models.TextField()