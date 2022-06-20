from django.urls import path

from .views import СommentView

urlpatterns = [
    path('api/v1/comments/', СommentView.as_view()),
]
