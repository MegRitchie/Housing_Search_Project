
# Forms code retrieved from : https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

from django import forms

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import fields, CheckboxInput

from .models import UserProfile, Review


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserProfileForm(forms.ModelForm):
    # avatar = forms.ImageField(required=False)
    # bio = forms.Textarea()

    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']

class ReviewForm(forms.ModelForm):
    review = forms.Textarea()
    
    class Meta:
        model = Review
        fields = ['review',]

