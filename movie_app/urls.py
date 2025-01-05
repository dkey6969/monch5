from django.urls import path
from .views import (
    DirectorListCreateAPIView, DirectorDetailAPIView,
    MovieListCreateAPIView, MovieDetailAPIView,
    ReviewListCreateAPIView, ReviewDetailAPIView
)

urlpatterns = [
    path('directors/', DirectorListCreateAPIView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]