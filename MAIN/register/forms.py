#Import the necessary modules and models
from django import forms
from main.models import Author

#Define UpdateForm class to update author profile
class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Author #Set the model to Author
        fields = ("fullname", "bio", "profile_pic") #Specify the fields to include in the form