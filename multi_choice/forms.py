from django.forms import ModelForm
from .models import Question, Story_text

class StoryForm(ModelForm):
    class Meta:
        model = Story_text
        fields = '__all__'
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'a', 'b', 'c', 'd', 'answer', 'marks']