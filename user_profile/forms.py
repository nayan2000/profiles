from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    f_name = forms.CharField(max_length=30, required=True, help_text='Optional.', label = 'First Name ')
    l_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label= 'Last Name ')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='Email ')
    github_profile = forms.CharField(max_length = 60,  required= False, help_text = 'Optional.',label = 'Github Profile Link ')
    reddit_profile = forms.CharField(max_length = 60, required= False, help_text = 'Optional.', label = 'Reddit Profile Link ')
    facebook_profile = forms.CharField(max_length = 60,  required= False, help_text = 'Optional.', label = 'Facebook Profile Link ')
    linkedin_profile = forms.CharField(max_length = 60, required= False, help_text = 'Optional.', label = 'LinkedIn Profile Link ')

    class Meta:
        model = User
        fields = ('username', 'f_name', 'l_name', 'email', 'password1', 'password2','github_profile', 'reddit_profile', 'facebook_profile', 'linkedin_profile' )
        
