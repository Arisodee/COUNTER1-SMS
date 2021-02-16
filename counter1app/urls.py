from django.conf.urls import url                                                                                                                                                         
from . import views
from django.urls import path


urlpatterns = [ 
    
    path('talking/', views.talking_view, name='lets_talk'),
    path('success_report/', views.success_report, name='success_report'),
    
    
]