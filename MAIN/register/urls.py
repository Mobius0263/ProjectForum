#Import the path function and views
from django.urls import path
from .views import signup, signin, update_profile, logout

#URL pattern for the register application
urlpatterns = [
    path("signup/", signup, name="signup"), #URL pattern for sign up view
    path("signin/", signin, name="signin"), #URL pattern for sign in view
    path("logout/", logout, name="logout"), #URL pattern for log out view
    path("update_profile/", update_profile, name="update_profile"), #URL pattern for updating a profile
]