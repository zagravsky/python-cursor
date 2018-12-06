from django import forms
from .models import Todo
from ckeditor_uploader.fields import RichTextUploadingFormField


class NewTodoForm(forms.ModelForm):
    text = RichTextUploadingFormField()

    class Meta:
        model = Todo
        fields = ('title', 'text',)
