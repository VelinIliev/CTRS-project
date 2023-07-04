from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase

from CTRS_course_project.user_app.forms import UserCreateStaffForm

UserModel = get_user_model()


class UserCreateStaffFormTest(TestCase):
    def test_staff_profile_save__is_staff__expect_correct_result(self):
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
        self.assertTrue(user.is_staff)

    def test_staff_profile_save__not_is_superuser_expect_correct_result(self):
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
        self.assertFalse(user.is_superuser)
