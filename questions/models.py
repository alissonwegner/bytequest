from django.db import models
from categorys.models import Categorys

# Create your models here.
class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_title= models.CharField(max_length=50)
    question_txt = models.TextField(max_length=500)
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT, related_name='category')

    class Meta:
        ordering = ['question_id']

    def __str__(self):
        return self.question_title

