from django.urls import path
from .views import PipelineView

urlpatterns = [
    path('', PipelineView.as_view()),
]
