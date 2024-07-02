#Import the path function and views
from django.urls import path
from .views import (
    home, detail, posts, create_post, latest_posts,
    search_result,)

#URL pattern for the application
urlpatterns = [
    path("", home, name="home"), #URL pattern for the home view
    path("detail/<slug>/", detail, name="detail"), #URL pattern for the detail view with a slug parameter
    path("posts/<slug>/", posts, name="posts"), #URL pattern for the posts view with a slug parameter
    path("create_post", create_post, name="create_post"), #URL pattern for the create_post view
    path("latest_posts", latest_posts, name="latest_posts"), #URL pattern for the latest_posts view
    path("search", search_result, name="search_result"), #URL pattern for the search_result view
]