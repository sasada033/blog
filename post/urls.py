from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('privacy/', views.PrivacyPolicyView.as_view(), name='privacy'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<str:tag>/', views.IndexView.as_view(), name='index_tag'),
    path('', views.IndexView.as_view(), name='index'),
]
