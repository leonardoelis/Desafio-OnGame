from django.urls import path, include
from .views import register_topic, show_topic, register_comment

urlpatterns = [
    path('register/', register_topic, name='register_topic'),
    path('<int:id>/', show_topic, name='show_topic'),
    path('<int:id>/register-comment/', register_comment, name='register_comment')
]
