#Import Django modules and dependencies
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#URL pattern for the admin interface
urlpatterns = [
    path('admin/', admin.site.urls), #Include the URL patterns from the main application (usually the homepage)
    path('', include("main.urls")), #Include the URL patterns for TinyMCE, a rich text editor
    path('tinymce/', include('tinymce.urls')), #Include the URL patterns for TinyMCE, a rich text editor
    path('account/', include('register.urls')), #Include the URL patterns from the register application (user accounts)
    path('hitcount/', include('hitcount.urls', namespace='hitcount')), #Include the URL patterns for the hitcount application (tracking views)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Serve media files during development