from django.urls import path
from . import views

urlpatterns = [
    path('', views.pipelines_list),
    path('<int:pk>', views.pipeline_edit),
    path('alpha/', views.alpha_view)
]
