from django.urls import path

from .views import TaskView

urlpatterns = [
    path('api/v1/tasks/', TaskView.as_view()),
]
