"""src/api URL Configuration
"""
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

from .views import UserView


urlpatterns = [
    path('users/', UserView.as_view()),
    path('login/', obtain_jwt_token),
]
