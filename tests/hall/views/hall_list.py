from django.test import TestCase
from django.urls import reverse

from CTRS_course_project.hall.models import Hall


class HallListViewTest(TestCase):
    def test_hall_list_view__when_no_halls__expect_empty_list(self):
        response = self.client.get(reverse('hall index'))
        self.assertEqual(0, len(response.context['halls']))

    def test_hall_list_view__when_halls__expect_halls_list_ordered_by_id_reverse(self):
        hall = Hall(
            name='Test Hall',
            rows=5,
            seats_per_row=5,
            description='Test description',
        )
        hall2 = Hall(
            name='Test Hall 2',
            rows=5,
            seats_per_row=5,
            description='Test description',
        )
        hall.save()
        hall2.save()
        response = self.client.get(reverse('hall index'))
        self.assertEqual(2, len(response.context['halls']))
        self.assertListEqual([hall2, hall], list(response.context['halls']))
