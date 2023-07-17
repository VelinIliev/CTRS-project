from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from CTRS_course_project.movies.models import Movie
from CTRS_course_project.user_app.forms import UserCreateStaffForm


class MovieViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.movie = Movie(
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
        self.movie.save()

    def test_movie_list_view(self):
        url = reverse('movies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)
        print(response)

    def test_movie_detail_view(self):
        url = reverse('details movie',
                      kwargs={'pk': self.movie.pk, 'slug': self.movie.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)
        self.assertEqual('Director 1, Director 2', response.context['movie'].directors)
        self.assertEqual(2021, response.context['movie'].year)
        self.assertEqual('https://example.com/image.jpg', response.context['movie'].image_url)
        self.assertEqual('2h 0min', response.context['runtime'])
        self.assertEqual('Test plot', response.context['movie'].plot)
        self.assertEqual(['Writer 1', 'Writer 2'], response.context['writers'])
        self.assertEqual(['Actor 1', 'Actor 2'], response.context['actors'])
        self.assertEqual('Genre 1, Genre 2', response.context['movie'].genres)
        self.assertEqual('Country', response.context['movie'].country)
        self.assertEqual('Language 1, Language 2', response.context['movie'].languages)
        self.assertEqual('PG-13', response.context['movie'].contentRating)
        self.assertEqual('https://www.imdb.com/movie', response.context['movie'].imbd_link)
        self.assertTrue(response.context['movie'].is_active)


