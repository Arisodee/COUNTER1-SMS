from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from counter1app.views import profile_upload
from counter1app import views
# from .views import delete_contact

urlpatterns = [
    path('', views.user_page, name="user_page"),
    path('add-contact/',views.addContact,name='add-contact'),
    # path('user_page/',views.user_page,name='user_page'),
    path('profile_upload/', profile_upload, name="profile_upload"),
    path('register_user/',views.register_user,name= 'register_user'),
    # path('user/delete/<int:pk>',views.delete_contact.as_view(),name='delete_contact'),
    path('update/<int:pk>/',views.update_contact.as_view(),name='update_contact'),
    
    
]
