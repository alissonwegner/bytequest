from django.db import models

# Create your models here.
class Users(models.Model):
    user_id =models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=50)

class Meta:
    ordering = ['user_id']

def __str__(self):
    return self.nome