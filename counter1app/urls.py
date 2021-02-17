from django.conf.urls import url                                                                                                                                                         
from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required


    
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url('^dashboard/$',views.dashboard,name='dashboard'),
    path('register', views.RegistrationView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('activate/<uidb64>/<token>',  views.ActivateAccountView.as_view(), name='activate'),
    path('set-new-password/<uidb64>/<token>',  views.SetNewPasswordView.as_view(), name='set-new-password'),
    path('request-reset-email', views.RequestResetEmailView.as_view(), name='request-reset-email'),
    # path('social-auth/', include('social_django.urls', namespace='social'))
    path('talking/', views.talking_view, name='lets_talk'),
    path('success_report/', views.success_report, name='success_report'),
    url('^user_page/$',views.user_page,name='user_page'),

]
