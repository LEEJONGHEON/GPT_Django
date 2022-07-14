from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=100)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일자
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_question')

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True) #수정일자
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Write(models.Model):
    content = models.CharField(max_length=100)
    create_content = models.TextField()