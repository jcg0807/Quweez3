from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Tweet
from phonenumber_field.formfields import PhoneNumberField as FormPhoneNumberField


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Job Title HERE'}),
        }

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','phone_number', 'email', 'password']

    class CustomRegistrationForm(forms.Form):

        first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
        last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    def clean_username(self):
        username = self.cleaned_data['username']
        forbidden_words = ['shit', 'fuck', 'bobo']
        for word in forbidden_words:
            if word in username.lower():
                raise ValidationError(f"Username cannot contain the word '{word}'.")
        return username

    phone_number = FormPhoneNumberField(required=False)

    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        allowed_domains = ['objor.com']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords don't match.")
        return cleaned_data

    def save(self, commit=True):
        # Get the unsaved User instance
        user = super().save(commit=False)
        # Hash the password
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user