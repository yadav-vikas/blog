from django.urls import path

from . import views

urlpatterns = [
    path('users/',views.UserListCreateAPIView.as_view()),
    path('user/<int:pk>/', views.UserRetrieveUpdateAPIView.as_view()),
]