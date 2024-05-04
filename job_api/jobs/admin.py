from django.contrib import admin
from .models import Job  # Updated import

admin.site.register(Job)  # Registering the Job model in the admin site
