from django.urls import path

from . import views

urlpatterns = [
    path('list/',views.BlogListAPIView.as_view()),
    path('get/<int:pk>/', views.BlogRetrieveAPIView.as_view()),
    path('update/<int:pk>/', views.BlogUpdateAPIView.as_view()),
    path('delete/<int:pk>/', views.BlogDestroyAPIView.as_view()),
]