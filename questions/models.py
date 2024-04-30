from django.db import models
from .models import Options, Categorys

# Create your models here.
class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_title= models.CharField(max_length=50)
    question_txt = models.TextField(max_length=500)
    correct_answer_id =  models.ForeignKey(Options, on_delete=models.PROTECT, related_name='correct_answer_id')
    category_id = models.ForeignKey(Categorys, on_delete=models.PROTECT, related_name='category_id')


class Meta:
    ordering = ['question_id']

def __str__(self):
    return self.questrion_clar

