from django.conf.urls import url                                                                                                                                                         
from . import views
from django.urls import path


urlpatterns = [ 
    # url(r'broadcast$', views.broadcast_sms, name="default"),

    path('talking/', views.talking_view, name='lets_talk'),
    
    
    
]