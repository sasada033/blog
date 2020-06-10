from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<str:tag>/', views.IndexView.as_view(), name='index_tag'),
]
