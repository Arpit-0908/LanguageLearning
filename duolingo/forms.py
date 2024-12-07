from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        min_length=8
    )
    password2 = forms.CharField(
        label='Confirm Password', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        min_length=8
    )
    full_name = forms.CharField(
        label='Full Name', 
        max_length=150, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'})
    )
    phone_number = forms.CharField(
        label='Phone Number', 
        max_length=15, 
        required=False,  # Optional field
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )
    
    # List of languages
    LANGUAGES = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('zh', 'Chinese'),
        ('ja', 'Japanese'),
        ('ru', 'Russian'),
        ('hi', 'Hindi'),
        ('ar', 'Arabic'),
        ('pt', 'Portuguese'),
    ]
    
    # Dropdown for language selection
    interested_language = forms.ChoiceField(
        choices=[('', 'Select a language')] + LANGUAGES,
        label='Interested in Learning a Language',
        required=False  # Optional field
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'phone_number']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

