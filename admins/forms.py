from django import forms
from django.db.models.base import Model

from users.forms import UserRegistrationForm, UsersProfileForm
from users.models import User


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'image')


class UserAdminProfileForm(UsersProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control py-4', 'readonly': False}))