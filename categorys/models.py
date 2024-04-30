from django.db import models

class Categorys(models.Model):
    category_id = models.AutoField(primary_key=True)
    categoria_txt = models.CharField(max_length=100)

class Meta:
    ordering = ['category_id']

def __str__(self):
    return self.category_id