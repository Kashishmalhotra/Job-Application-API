from rest_framework import serializers
from .models import Job  # Updated import

class JobSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Job 
        fields = ['title', 'description', 'company', 'location', 'created_at', 'is_active']  # Updated fields according to the Job model
