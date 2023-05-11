from django.shortcuts import render

from rest_framework import viewsets
from .serializers import blogSerializer
from .models import blog


class blogView(viewsets.ModelViewSet):
    serializer_class = blogSerializer
    queryset = blog.objects.all()
