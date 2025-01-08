from django.contrib import admin
from movie_app.models import  Director, SearchWord, Movie, Review

admin.site.register(Director)
admin.site.register(SearchWord)
admin.site.register(Movie)
admin.site.register(Review)

