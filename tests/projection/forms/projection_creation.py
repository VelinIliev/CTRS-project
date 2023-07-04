from django.contrib.auth import get_user_model
from django.test import TestCase

from CTRS_course_project.hall.models import Hall
from CTRS_course_project.movies.models import Movie
from CTRS_course_project.projection.forms import CreateProjectionForm
from CTRS_course_project.projection.models import Seat

UserModel = get_user_model()


class CreateProjectionFormTest(TestCase):
    def setUp(self):
        self.hall = Hall(
            name="testname",
            rows=5,
            seats_per_row=5,
            description="test descr"
        )
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
        self.hall.save()
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.projection_data = {
            'date': '2023-07-04',
            'hour': '12:30',
            'hall': self.hall,
            'movie': self.movie,
        }

    def test_create_projection_form(self):
        form = CreateProjectionForm(data=self.projection_data)
        self.assertTrue(form.is_valid())

        projection = form.save()

        self.assertEqual(projection.date.strftime('%Y-%m-%d'), '2023-07-04')
        self.assertEqual(projection.hour.strftime('%H:%M'), '12:30')
        self.assertEqual(projection.hall_id, self.hall.id)  # Verify the hall ID is set correctly

        seats = Seat.objects.filter(projection_id=projection.id)
        self.assertEqual(seats.count(), projection.hall.rows * projection.hall.seats_per_row)
