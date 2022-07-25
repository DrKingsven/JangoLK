from django.urls import path

from .views import *

urlpatterns = [
    path('api/v1/tasks/', TaskAPICreate.as_view()),
    path('api/v1/tasks/<int:pk>/', TaskAPIUpdate.as_view()),
]
