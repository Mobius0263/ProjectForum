#Import Django module and models
from django.contrib import admin
from .models import Category, Author, Post, Comment, Reply

# Register your models here.
admin.site.register(Category) #Registering the Category model with the admin site
admin.site.register(Author) #Registering the Author model with the admin site
admin.site.register(Post) #Registering the Post model with the admin site
admin.site.register(Comment) #Registering the Comment model with the admin site
admin.site.register(Reply) #Registering the Reply model with the admin site