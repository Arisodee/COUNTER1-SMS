from django.urls import path
from .api import ContactCreateApi,ContactApi,ContactUpdateApi,ContactDeleteApi



urlpatterns = [
    path('api',ContactApi.as_view()),
    path('api/create',ContactCreateApi.as_view()),
    path('api/<int:pk>',ContactUpdateApi.as_view()),
    path('api/<int:pk>/delete',ContactDeleteApi.as_view()),
]