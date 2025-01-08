from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


class MovieReviewList(generics.ListAPIView):
    queryset = Movie.objects.prefetch_related('reviews')
    serializer_class = MovieSerializer


class DirectorList(generics.ListAPIView):
    queryset = Director.objects.annotate(movies_count=Count('movies'))
    serializer_class = DirectorSerializer


class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
