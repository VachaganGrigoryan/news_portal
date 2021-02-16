from django.urls import path
from categories import views

urlpatterns = [
    path('<int:pk>-<str:slug>/', views.category_detail, name='category-detail')
]
