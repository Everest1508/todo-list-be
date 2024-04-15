from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Task

# Create your views here.
class TaskViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()