from django import forms
from .models import Topic

#Topicモデルの制約を元にバリデーションルール(フォームクラス)を作る
class TopicForm(forms.ModelForm):
    class Meta:
        model   = Topic
        fields  = ["comment","name"]

