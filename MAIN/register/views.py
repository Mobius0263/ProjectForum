from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from register.forms import UpdateForm
from django.contrib.auth import logout as lt
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from main.models import Author
from django.utils.text import slugify

# Create your views here.
def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("update_profile")
    context.update({
        "form": form,
        "title":"Signup",
    })
    return render(request, "register/signup.html", context)

def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=user, password=password)
        if user is not None:
            return redirect("home")
    context.update({
        "form":form,
        "title":"Signin",
    })
    return render(request, "register/signin.html", context)

@login_required
def update_profile(request):
    context = {}
    user = request.user
    author, created = Author.objects.get_or_create(user=user)
    form = UpdateForm(request.POST or None, request.FILES or None, instance=author)
    if request.method == "POST":
        if form.is_valid():
            try:
                author = form.save(commit=False)
                author.slug = slugify(author.fullname)
                author.save()
                return redirect("home")
            except IntegrityError:
                messages.error(request, 'This slug is already in use. Please choose another one.')
    context.update({
        "form":form,
        "title":"Update Profile",
    })
    return render(request, "register/update.html", context)

@login_required
def logout(request):
    lt(request)
    return redirect("home")