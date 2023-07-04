from django.core.exceptions import ValidationError
from django.test import TestCase

from CTRS_course_project.movies.models import Movie


class MovieModelTest(TestCase):

    def test_movie_creation__slug_creation__expect_everything_to_be_correct(self):
        movie = Movie(
            title='Test Movie',
            year=2021,
            image_url='https://example.com/image.jpg',
            runtime=120,
            plot='Test plot',
            directors='Director 1, Director 2',
            writers='Writer 1, Writer 2',
            actors='Actor 1, Actor 2',
            genres='Genre 1, Genre 2',
            country='Country',
            languages='Language 1, Language 2',
            contentRating='PG-13',
            imbd_link='https://www.imdb.com/movie',
            is_active=True,
        )
        movie.save()
        self.assertEqual(movie.slug, 'test-movie-2021')

    def test_movie_creation__with_invalid_movie_year__expect_validation_error(self):
        movie = Movie(
            title='Test Movie',
            year=1800,
            image_url='https://example.com/image.jpg',
            runtime=120,
            plot='Test plot',
            directors='Director 1, Director 2',
            writers='Writer 1, Writer 2',
            actors='Actor 1, Actor 2',
            genres='Genre 1, Genre 2',
            country='Country',
            languages='Language 1, Language 2',
            contentRating='PG-13',
            imbd_link='https://www.imdb.com/movie',
            is_active=True,
        )

        with self.assertRaises(ValidationError) as ve:
            movie.full_clean()
            movie.save()
        self.assertEqual("{'year': ['There was no cinema back then.']}", str(ve.exception))