from django.urls import path

from .views import –°ommentView

urlpatterns = [
    path('api/v1/comments/', –°ommentView.as_view()),
]
