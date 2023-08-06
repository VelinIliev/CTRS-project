from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_after_registration(instance, created, **kwargs):
    if not created:
        return

    # user_email = instance.email

    # send_mail(
    #     subject='Welcome to CTRS ARENA!',
    #     message="Welcome to CTRS (Cinema Tickets Reservation System)! "
    #             "We're delighted to have you here. With CTRS, your movie ticket booking "
    #             "experience is about to reach new heights. Say goodbye to long queues and "
    #             "last-minute disappointments. Get ready to indulge in seamless ticket "
    #             "reservations and secure your spot for an extraordinary cinematic adventure. "
    #             "Sit back, relax, and let CTRS take care of all your movie-going needs. Enjoy the show!",
    #     from_email=settings.DEFAULT_FROM_EMAIL,
    #     recipient_list=(user_email, ),
    # )
