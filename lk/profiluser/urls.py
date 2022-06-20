from django.urls import path

from .views import ProfiluserView

urlpatterns = [
    path('api/v1/profilusers/', ProfiluserView.as_view()),
]
