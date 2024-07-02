#Import the AppConfig class from django.apps
from django.apps import AppConfig

#Define RegisterConfig class as register configuration
class RegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #Set the default auto field type for the primary key
    name = 'register' #Define the name of the application
