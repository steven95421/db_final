from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Home.models import event
from Home.models import Team
from django.forms import ModelForm
from django.forms import modelformset_factory


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
                  'email', 'password1', 'password2',)


class EventForm(ModelForm):
    class Meta:
        model = event
        fields = '__all__'
        widgets = {
            'Date': forms.DateTimeInput(attrs={'class': 'datetimepicker'})
        }
    

class EventSignUp(ModelForm):
    #event_id = forms.IntegerField("self",blank = True) 
    class Meta:
        model = Team
        fields = ('team_name','student_id','student_name')
        widgets = {
            'team_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Team Name here'
                }
            )
        }

MemberFormset = modelformset_factory(
    Team,
    fields=('student_id','student_name', ),
    extra=1,
    widgets={
        'student_id': forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'student_name': forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    }
)

