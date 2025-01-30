from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from .models import *

# Register Form
class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email']
        labels = {
            'username': "Foydalanuvchi nomi",
            'email': "Elektron pochta manzili"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': "form-control form-control-lg"})
        self.fields['email'].widget.attrs.update({'class': "form-control form-control-lg"})
        self.fields['password1'].widget.attrs.update({'class': "form-control form-control-lg"})
        self.fields['password2'].widget.attrs.update({'class': "form-control form-control-lg"})



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Login Form:
class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        username = self.fields['username']
        password = self.fields['password']

        username.label = "Foydalanuvchi nomi"
        username.widget.attrs.update({
            'class': "form-control",
            'placeholder': "Foydalanuvchi nomingizni kiriting"
        })
        password.label = "Password kiriting"
        password.widget.attrs.update({
            'class': "form-control",
            'placeholder': "Parolingizni kiriting"
        })
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Comment Form:
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': "form-control"
            })
        }

    def save(self, comment, user, lesson):
        comment.objects.create(
            text=self.cleaned_data.get('text'),
            author=user,
            lesson=lesson
        )

    def update(self, value):
        value.text = self.cleaned_data.get('text')
        value.save()