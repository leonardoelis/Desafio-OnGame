from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_user, edit_user, change_password

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_user, name='register_user'),
    path('edit/', edit_user, name='edit_user'),
    path('change-password/', change_password, name='change_password')
]
