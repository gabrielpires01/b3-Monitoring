from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import PipelineSerializer
from .models import Pipeline
from rest_framework.response import Response
from rest_framework import status
from .alpha_api import get_alpha_api, get_alpha_api_last

import requests


@api_view(['GET', 'POST'])
def pipelines_list(request):
    if request.method == 'GET':
        data = Pipeline.objects.all()

        serializer = PipelineSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        alpha_data = get_alpha_api_last(data['interval'], data['symbol'])
        data['current_value'] = alpha_data['4. close']

        serializer = PipelineSerializer(data=data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def alpha_view(request, *args, **kwargs):
    params = request.query_params

    data = get_alpha_api(params['interval'], params['symbol'])
    print(data)

    if data is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(data)

