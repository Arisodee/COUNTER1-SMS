from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views as user_views


urlpatterns=[
    path('',views.index,name = 'index'),
    path('accounts/register/', views.register, name='register'),
    path('create_user/', user_views.create_user,name = 'create'),
    url(r'^editSupervisor/(\d+)', views.edit_superlist, name='editSupervisor'),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)