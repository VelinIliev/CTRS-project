from django.core.exceptions import ValidationError
from django.test import TestCase

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ProfileModelTests(TestCase):
    def test_profile_save__with_first_name_only_letters__expect_correct_result(self):
        profile = UserModel(
            username="test40",
            password="GoodPass123!",
            age=22,
            email="test40@abv.bg",
            first_name="testname",
            last_name="testname",
        )
        profile.full_clean()
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_save__with_first_name_with_numbers__expect_validation_error(self):
        profile = UserModel(
            username="test40",
            password="GoodPass123!",
            age=22,
            email="test40@abv.bg",
            first_name="testname40",
            last_name="testname",
        )

        with self.assertRaises(ValidationError) as ve:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(ve.exception)
