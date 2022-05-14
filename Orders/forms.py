from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationform(UserCreationForm):
    email = forms.EmailField(max_length=300,required=True,help_text="Inform a valid EMail ID")
    address = forms.CharField(max_length=300)
    city = forms.CharField(max_length=50)
    zipcode = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'address', 'city', 'zipcode', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
