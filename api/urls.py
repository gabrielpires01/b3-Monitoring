from django.urls import path
from . import views

urlpatterns = [
    path('', views.pipelines_list),
    path('alpha/', views.alpha_view)
]
