from rest_framework import serializers
from .models import Pipeline

class PipelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipeline
        fields = ("id", "top_value", "bottom_value", "current_value", "symbol", "interval" ,"created_at")