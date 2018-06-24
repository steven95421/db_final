from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    studnet_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    gender = forms.ChoiceField(
         choices=(('m', 'Male'), ('f', 'Female')))
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'studnet_name','gender',
                  'email', 'password1', 'password2', )
                
