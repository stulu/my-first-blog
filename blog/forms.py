from django import forms
from ckeditor.fields import RichTextField
from .models import Post
#from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    text = RichTextField()

    class Meta:
        model = Post
        fields = ('title', 'text',)