from django.db import models

# Create your models here.
class Categories(models.Model):
    
    name = models.CharField()
    
class Tovar(models.Model):
    
    name = models.CharField()
    categories = models.ManyToManyField('Categories', db_column='cat_id')