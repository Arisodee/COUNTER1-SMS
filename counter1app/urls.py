
from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required
from .views import HomeView
from . import views
from django.conf.urls import url
from . import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register', views.RegistrationView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('activate/<uidb64>/<token>',  views.ActivateAccountView.as_view(), name='activate'),
    path('set-new-password/<uidb64>/<token>',  views.SetNewPasswordView.as_view(), name='set-new-password'),
    path('request-reset-email', views.RequestResetEmailView.as_view(), name='request-reset-email'),
    path('',HomeView.as_view(), name='main'),
    path('',views.index,name = 'index'),
    path('accounts/register/', views.register, name='register'),
    path('create_user/', user_views.create_user,name = 'create'),
    url(r'^editSupervisor/(\d+)', views.edit_superlist, name='editSupervisor'),
   
    # path('social-auth/', include('social_django.urls', namespace='social'))
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
