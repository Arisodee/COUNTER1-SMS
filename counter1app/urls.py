from django.conf import settings
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.homepage,name = 'homepage'),
    # path('search',views.search_group,name = 'search'),
]