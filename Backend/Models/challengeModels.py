from django.db import models
from enum import Enum
from ..models import Company


class Challenge(models.Model):
    challenge_id=models.AutoField(primary_key=True)
    challenge_name=models.CharField(max_length=100)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    challenge_time=models.IntegerField(default=0)
    login_window=models.IntegerField(default=0)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='challenge',null=True)

    def __str__(self) -> str:
        return self.challenge_name



class MCQ(models.Model):
    mcq_id=models.AutoField(primary_key=True)
    q_name=models.CharField(max_length=100)
    statement=models.TextField()
    score=models.IntegerField()
    q_options=models.JSONField(default=dict)
    correctOptions=models.JSONField(default=dict)
    challenge=models.ForeignKey(Challenge,on_delete=models.CASCADE,related_name='mcq',null=True)


    def __str__(self) -> str:
        return self.q_name
    

class Coding(models.Model):
    problem_id=models.AutoField(primary_key=True)
    problem_name=models.CharField(max_length=100)
    score=models.IntegerField()
    languages=models.JSONField(default=dict)
    challenge=models.ForeignKey(Challenge,on_delete=models.CASCADE,related_name='coding',null=True)

    def __str__(self) -> str:
        return self.problem_name
    
class TestCase(models.Model):

    class Difficulty(Enum):
        EASY='easy'
        MEDIUM='medium'
        HARD='hard'

        @classmethod
        def choices(cls):
            return [(item.name,item.value) for item in cls]


    testcase_id=models.AutoField(primary_key=True)
    testcase_name=models.CharField(max_length=100)
    difficulty=models.CharField(max_length=6,choices=Difficulty.choices())
    problem=models.ForeignKey(Coding,on_delete=models.CASCADE,related_name='testcase',null=True)
    testcase=models.TextField()
    output=models.TextField(default="")
    is_sample=models.BooleanField(default=False)
