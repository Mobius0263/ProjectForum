#Import the AppConfig class from django.apps
from django.apps import AppConfig 

#Define MainConfig class as application configuration
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #Set the default auto field type for the primary key
    name = 'main' #Define the name of the application
