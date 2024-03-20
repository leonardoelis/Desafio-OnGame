from django import forms
from .models import Topic, Comment


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'category', 'image', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Assunto'}),
            'category': forms.TextInput(attrs={'placeholder': 'Categoria'}),
            'message': forms.Textarea(attrs={'placeholder': 'Insira sua mensagem aqui'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Insira seu comentário aqui'})
        }
