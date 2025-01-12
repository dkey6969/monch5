from django.urls import path
from .views import (
    MovieReviewList,
    DirectorList,
    DirectorDetailAPIView,
    MovieListCreateAPIView,
    ReviewListCreateAPIView,
    DirectorViewSet,
)

urlpatterns = [

    path('api/v1/movies/reviews/', MovieReviewList.as_view(), name='movie-reviews'),

    path('api/v1/directors/', DirectorList.as_view(), name='directors'),

    path('api/v1/directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),


    path('api/v1/directors/', DirectorList.as_view(), name='directors'),


    path('api/v1/directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),


    path('api/v1/movies/', MovieListCreateAPIView.as_view(), name='movie-list'),


    path('api/v1/reviews/', ReviewListCreateAPIView.as_view(), name='review-list'),


]