from django import forms
from .models import Question, Answer, Write


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': '제목',
            # 'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = ['content', 'create_content']
        labels = {
            'content': '키워드',
            'create_content' : '생성내용',
        }