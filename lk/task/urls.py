from django.urls import path

from .views import TaskAPIView

urlpatterns = [
    path('api/v1/tasks/', TaskAPIView.as_view()),
]
