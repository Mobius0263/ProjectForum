#Import necessary modules from Django and other libraries
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from register.forms import CustomUserCreationForm, UpdateForm
from django.contrib.auth import logout as lt
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from main.models import Author
from django.utils.text import slugify

#signup view
def signup(request):
    context = {} #Initialize an empty context dictionary
    form = CustomUserCreationForm(request.POST or None) #Instantiate a UserCreationForm with POST data if available
    if request.method == 'POST': #Check if the request method is POST
        if form.is_valid(): #Check if the form is valid
            new_user = form.save() #Save the new user
            auth_login(request, new_user) #Log in the new user
            return redirect("update_profile") #Redirect to the update_profile view
    context.update({
        "form": form,
        "title":"Signup",
    }) #Update the context with the form and title
    return render(request, "register/signup.html", context) #Render the signup template with the context

#signin view
def signin(request):
    context = {} #Initialize an empty context dictionary
    form = AuthenticationForm(request, data=request.POST) #Instantiate an AuthenticationForm with POST data if available
    if form.is_valid(): #Check if the form is valid
        user = form.get_user()  # Get the authenticated user
        auth_login(request, user)  # Log in the user
        next_url = request.GET.get('next', 'home')  # Get the 'next' URL parameter or default to 'home'
        return redirect(next_url)  # Redirect to the 'next' URL
    context.update({
        "form":form,
        "title":"Signin",
    }) #Update the context with the form and title
    return render(request, "register/signin.html", context) #Render the signin template with the context

#Login requirement for update_profile view
@login_required
def update_profile(request):
    context = {} #Initialize an empty context dictionary
    user = request.user #Get the current logged-in user
    author, created = Author.objects.get_or_create(user=user) #Get or create an Author object for the user
    form = UpdateForm(request.POST or None, request.FILES or None, instance=author) #Instantiate the UpdateForm with POST and FILES data if available, and the author instance
    if request.method == "POST": #Check if the request method is POST
        if form.is_valid(): #Check if the form is valid
            try:
                author = form.save(commit=False) #Save the form data without committing to the database
                author.slug = slugify(author.fullname) #Generate a slug from the author's fullname
                author.save() #Save the author object to the database
                return redirect("home") #Redirect to the home view
            except IntegrityError:
                messages.error(request, 'This slug is already in use. Please choose another one.') #Display an error message if the slug is already in use
    context.update({
        "form":form,
        "title":"Update Profile",
    }) #Update the context with the form and title
    return render(request, "register/update.html", context) #Render the update_profile template with the context

#Login requirement for logout view
@login_required
def logout(request):
    lt(request) #Log out the user
    return redirect("home") #Redirect to the home view