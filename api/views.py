from django.shortcuts import render
from rest_framework import generics
from .serializers import PipelineSerializer
from .models import Pipeline

class PipelineView(generics.CreateAPIView):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer