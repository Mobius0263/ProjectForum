#Import the necessary modules and models
from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.models import User
from main.models import Author
from django.core.exceptions import ValidationError

# Define a custom user creation form with email field
class CustomUserCreationForm(BaseUserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Fill in a valid email address.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
#Define UpdateForm class to update author profile
class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Author #Set the model to Author
        fields = ("fullname", "bio", "profile_pic") #Specify the fields to include in the form