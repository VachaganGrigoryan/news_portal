from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<int:pk>-<str:slug>/', views.post_detail, name='post-detail'),
    path('404/', views.handle_404, name="handle-404"),
]
