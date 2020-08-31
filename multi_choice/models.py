from django.db import models
from django.contrib.auth.models import User
from random import shuffle

# Create your models here.


class Story_text(models.Model):
   title = models.CharField(max_length=70)
   body = models.TextField(max_length=700)

   def __str__(self):
      return str(self.title)


class Question(models.Model):
    story = models.ForeignKey(Story_text, null=True, on_delete=models.CASCADE)
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    a = models.CharField(max_length=200, default="", unique=False)
    b = models.CharField(max_length=200, default="",unique=False)
    c = models.CharField(max_length=200, default="",unique=False)
    d = models.CharField(max_length=200, default="",unique=False    )
    answer = models.CharField(max_length=200)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text


