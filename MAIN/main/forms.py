#Import the necessary modules and libraries
from django import forms
from tinymce.widgets import TinyMCE
from .models import Post

#Define a form for creating ad editing Posts
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})) #Character field for the content of the post
    
    class Meta:
        model = Post #Specify the model to use this form
        fields = ['title', 'content', 'image', 'categories', 'tags'] #Specify the fields to include in the form