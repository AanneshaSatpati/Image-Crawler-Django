from django.db import models

# Create your models here.
class User(models.Model):
    userEmail = models.CharField(max_length=200)
    

class Choice(models.Model):
    #question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)