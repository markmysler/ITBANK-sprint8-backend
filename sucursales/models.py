from django.db import models

# Create your models here.

class Sucursal(models.Model):
    branch_id= models.AutoField(primary_key=True, auto_created=True)
    country= models.TextField(null=False)
    region= models.TextField(null=False)
    city= models.TextField(null=False)
    address= models.TextField(null=False)