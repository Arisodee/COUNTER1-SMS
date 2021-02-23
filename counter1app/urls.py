from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from counter1app.views import profile_upload
from counter1app import views
from .views import GroupUpdateView,GroupDeleteView,SmsNumJsonView
# from .views import delete_contact

urlpatterns = [
    path('', views.user_page, name="user_page"),
    path('add-contact/',views.addContact,name='add-contact'),
    path('profile_upload/', profile_upload, name="profile_upload"),
    path('register_user/',views.register_user,name= 'register_user'),
    path('update/<int:pk>/',views.update_contact.as_view(),name='update_contact'),
    path('updategroup/', views.updategroup,name="update"),
    path('deletegroup/', views.deletegroup,name="delete"),
    path('post/<int:pk>/update/',GroupUpdateView.as_view(), name="updateForm"),
    path('post/<int:pk>/delete/',GroupDeleteView.as_view(), name="deleteForm"),
    path('sms-json/',SmsNumJsonView.as_view(),name = 'sms-json'),
    path('search',views.search_results,name = 'search_results'),
  ] 
# + static(settings.STATIC_URL, doument_root=settings.STATIC_ROOT)

    
    









  