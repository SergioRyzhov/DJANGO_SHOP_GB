from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from datetime import date
from django.core.exceptions import ValidationError

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'py-4'}), required=False)
    birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите дату рождения'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'image', 'birth')

    def clean_birth(self):
        today = date.today()
        birth = self.cleaned_data['birth']
        if today.year - birth.year < 18:
            # raise ValidationError('18 years exception')
            self.add_error("birth", "Нет 18ти")
        return birth

class UsersProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')