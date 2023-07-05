from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from CTRS_course_project.user_app.forms import UserCreateStaffForm

UserModel = get_user_model()


class UserAuthTest(TestCase):
    def test_profile__when_anonymous_user__expect_user_to_be_anonymous(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(str(response.context['user']), "AnonymousUser")
        print(response.context['user'])

    def test_profile__when_logged_in_user__expect_user_to_be_correct(self):
        credentials = {
            'username': 'test90',
            'password': 'GoodPass123!',
        }
        user = UserModel.objects.create(username=credentials['username'])
        user.set_password(credentials['password'])
        user.save()

        self.client.login(**credentials)

        response = self.client.get(reverse('index'))
        self.assertEqual('test90', str(response.context['user']))
        self.assertEqual(False, response.context['user'].is_staff)

    def test_profile__when_logged_in_staff_user__expect_user_is_staff_to_be_correct(self):
        group1 = Group.objects.create(name='Group1')
        group2 = Group.objects.create(name='Group2')

        form = UserCreateStaffForm(
            data={
                'username': "test40",
                "password": "GoodPass123!",
                "email": "test@example.com",
                'groups': [group1.id, group2.id],
            })
        self.assertTrue(form.is_valid())
        user = form.save()

        self.client.login(username="test40", password='GoodPass123!')
        response = self.client.get(reverse('index'))

        self.assertEqual('test40', response.context['user'].username)
        self.assertEqual(True, response.context['user'].is_staff)
