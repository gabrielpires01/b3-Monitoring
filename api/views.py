from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import PipelineSerializer
from .models import Pipeline
from rest_framework.response import Response
from rest_framework import status
from .alpha_api import get_alpha_api, get_alpha_api_last
from .schedular import schedule

import requests


@api_view(['GET', 'POST'])
def pipelines_list(request):
    if request.method == 'GET':
        data = Pipeline.objects.all()

        serializer = PipelineSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PipelineSerializer(data=data)
        schedular = schedule()

        if serializer.is_valid():
            alpha_data = get_alpha_api_last(data['interval'], data['symbol'])

            schedule.add_job()
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def alpha_view(request):
    params = request.query_params

    data = get_alpha_api(params['interval'], params['symbol'])

    if data is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(data)

@api_view(['GET', 'DELETE'])
def pipeline_edit(request, pk):
    try:
        pipeline = Pipeline.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PipelineSerializer(pipeline)
        
        return Response(serializer.data)

    if request.method == 'DELETE':
        pipeline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)