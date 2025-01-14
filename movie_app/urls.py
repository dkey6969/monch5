from django.urls import path
from .views import (
    DirectorListCreateView, DirectorDetailView,
    MovieListCreateView, MovieDetailView,
    ReviewListCreateView, ReviewDetailView
)

urlpatterns = [
    path('api/v1/directors/', DirectorListCreateView.as_view(), name='director-list'),
    path('api/v1/directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('api/v1/movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('api/v1/movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('api/v1/reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('api/v1/reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]