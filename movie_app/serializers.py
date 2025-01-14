from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Имя режиссера должно содержать не менее 3 символов.")
        return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Название фильма должно содержать не менее 2 символов.")
        return value

    def validate_release_year(self, value):
        if value > 2025:
            raise serializers.ValidationError("Год выпуска не может быть больше 2025.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if not (1 <= value <= 10):
            raise serializers.ValidationError("Рейтинг должен быть в диапазоне от 1 до 10.")
        return value
