from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from .serializers import TodoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    queryset= Todo.objects.all()
    serializer_class= TodoSerializer
    permission_classes=[permissions.IsAuthenticated]
    allowed_methods=['GET','POST','PUT','DELETE']