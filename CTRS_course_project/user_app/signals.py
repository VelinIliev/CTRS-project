from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_after_registration(instance, created, **kwargs):
    if not created:
        return

    user_email = instance.email
    html_template = 'email_template.html'
    html_message = render_to_string(html_template, {'name': instance.username})

    subject = 'Welcome to CTRS ARENA!'
    from_email = 'info@veliniliev.eu'
    # recipient_list = (user_email,)

    message = EmailMessage(subject, html_message, from_email, [user_email, ])
    message.content_subtype = 'html'
    message.send()
