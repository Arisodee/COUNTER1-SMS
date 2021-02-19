from django.conf.urls import url
from django.urls import path,include
from . import views


urlpatterns = [
  url(r'^$', views.index, name="index"),
  url('^user_page/$',views.user_page,name='user_page'),
  path('',views.homepage,name = 'homepage'),
  # path('search',views.search_group,name = 'search'), 
  path('sms-json/', SmsNumJsonView.as_view(), name='sms-json'), 
  path('talking/', views.talking_view, name='lets_talk'),


]