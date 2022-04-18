from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model= User
        fields=('username', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user=super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model=NeighbourHood
        fields=['name', 'location', 'occupants_count', 'neighbourhood_photo', 'health_no', 'police_no']
