from django.db import models

# Create your models here.

class Statistic_quest(models.Model):
    statistic_id = models.AutoField(primary_key=True) 
    date = models.DateTimeField()
    total_questions = models.IntegerField(validators=[MaxValueValidator(100)])
    correct_answers = models.IntegerField(validators=[MaxValueValidator(100)])
    incorrect_answers = models.IntegerField(validators=[MaxValueValidator(100)])
    percentage_correct  = models.DecimalField(max_digits=5, decimal_places=2)
    total_all_questions = models.IntegerField()
    total_all_correct_answers = models.IntegerField()
    total_all_incorrect_answers = models.IntegerField()
    
class Meta:
    ordering = ['date']

def __str__(self):
    return self.statistic_id