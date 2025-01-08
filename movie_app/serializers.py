from rest_framework import serializers
from .models import Director, Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars']


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'reviews', 'rating']

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return round(sum(review.stars for review in reviews) / reviews.count(), 2)
        return None


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source='movies.count', read_only=True)

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']