from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=50, default="Unknown")
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class SearchWord(Director):
    pass

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    search_words = models.ManyToManyField(SearchWord, blank=True)

    def __str__(self):
        return self.title

STARS = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *'),
)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=5)

    def __str__(self):
        return f"Review for {self.movie.title} - {self.stars}stars"







