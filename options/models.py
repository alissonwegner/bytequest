from django.db import models
from questions.models import Questions
# Create your models here.
class Options(models.Model):
    option_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option_text = models.TextField(max_length=500)
    is_correct = models.BooleanField(default=False) 

    class Meta:
        ordering = ['option_id']

    def __str__(self):
        return self.question_text