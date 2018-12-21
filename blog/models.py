from django.db import models
from django.utils import timezone
from django import forms
#from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = RichTextUploadingField(blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

