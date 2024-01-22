from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', views.UserPasswordChange.as_view(), name='change_password'),
    path('profile/change-password-without-old/', views.change_password_without_old, name='change_password_without_old'),
    path('profile/reset-password/', views.UserPasswordReset.as_view(), name='reset_password'),
]