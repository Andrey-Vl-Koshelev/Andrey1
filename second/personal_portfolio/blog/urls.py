from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]