from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$', views.index, name="index"),
  url('^user_page/$',views.user_page,name='user_page'),
]