from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
from .forms import LoginForm

app_name = 'app_auth'

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name="signup"),  # app_quotes:home
    path('signin/', LoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm,),  name="signin"),
    path('logout/', LogoutView.as_view(template_name='app_auth/logout.html'), name="logout"),
    path('reset-password/', views.ResetPasswordView.as_view(template_name='app_auth/password_reset.html'),
         name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='app_auth/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='app_auth/password_reset_confirm.html',
                                          success_url='auth/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='app_auth/password_reset_complete.html'),
         name='password_reset_complete'),
]

