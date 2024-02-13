from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput, DateInput
from quotes.models import Author, Quote


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=55, required=True, widget=TextInput())
    born_date = CharField(min_length=5, max_length=25, required=True, widget=DateInput())
    born_location = CharField(min_length=5, max_length=65, required=True, widget=TextInput())
    description = CharField(min_length=10,   required=True, widget=forms.Textarea(attrs={'rows': 10}))
    class Meta:
        model = Author
        fields = ['fullname','born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    quote = CharField(min_length=10,   required=True, widget=forms.Textarea(attrs={'rows': 3}))
    tags = CharField(min_length=1, max_length=25, required=True, widget=TextInput())
    author = CharField(min_length=2, max_length=65, required=True, widget=TextInput())
    class Meta:
        model = Quote
        fields = ['quote']
        exclude = ['tags', 'author']




    

