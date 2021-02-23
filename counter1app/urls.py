from django.conf.urls import url
from django.conf import settings
from django.urls import path,include
from . import views
from .views import GroupUpdateView,GroupDeleteView,SmsNumJsonView
from django.conf.urls.static import static


urlpatterns = [
  # path('', views.index, name="index"),
  path('',views.user_page,name='user_page'),
  path('updategroup/', views.updategroup,name="update"),
  path('deletegroup/', views.deletegroup,name="delete"),
  path('post/<int:pk>/update/',GroupUpdateView.as_view(), name="updateForm"),
  path('post/<int:pk>/delete/',GroupDeleteView.as_view(), name="deleteForm"),
  path('sms-json/',SmsNumJsonView.as_view(),name = 'sms-json'),
  path('search',views.search_results,name = 'search_results'),
] + static(settings.STATIC_URL, doument_root=settings.STATIC_ROOT)