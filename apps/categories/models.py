from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length = 30,)

class Categories_1(models.Model):
    parent = models.ForeignKey(Categories, on_delete = True)

class Categories_1_1(models.Model):
    parent = models.ForeignKey(Categories_1, on_delete = True)

class Sale(models.Model,):
    parent = models.ForeignKey(Categories_1_1,on_delete = True )
