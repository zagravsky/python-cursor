# coding=utf-8
from django import forms
from .models import Todo, Profile
from ckeditor_uploader.fields import RichTextUploadingFormField


class NewTodoForm(forms.ModelForm):
    text = RichTextUploadingFormField()

    class Meta:
        model = Todo
        exclude = ['created_by']


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username")
    first_name = forms.CharField(label=u"First Name")
    last_name = forms.CharField(label="Second Name")
    email = forms.EmailField(label="Email", required=False)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
                self.add_error("password_confirm", "Passwords are different")
                return False
            elif len(self.cleaned_data['password']) < 5:
                self.add_error('password', "Password is too short")
        return valid


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
