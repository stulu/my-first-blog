from django import forms

from .models import Post
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('title', 'text',)