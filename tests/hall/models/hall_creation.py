from django.test import TestCase

from CTRS_course_project.hall.models import Hall


class HallModelTest(TestCase):
    def test_slug_generation(self):
        hall = Hall(
            name='Test Hall',
            rows=5,
            seats_per_row=5,
            description='Test description',
        )
        hall.save()

        self.assertEqual(hall.slug, 'test-hall-1')
