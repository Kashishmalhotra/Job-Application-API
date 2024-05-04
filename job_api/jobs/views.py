from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job  
from .serializers import JobSerializer 

class JobDetails(APIView):  
    def get(self, request, title):
        try:
            job = Job.objects.get(title=title)  # Updated variable name from "Job" to "job"
            serializer = JobSerializer(job)
            return Response(serializer.data)
        except Job.DoesNotExist:
            return Response({"message": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
