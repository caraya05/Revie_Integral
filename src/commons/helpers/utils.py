from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def send_mail_forgot(email_receives: str, message: str, subject: str):
    email_destination = settings.EMAIL_HOST_USER
    mail = EmailMultiAlternatives(
        subject=subject,
        body=message,
        from_email=email_destination,
        to=[email_receives],
        reply_to=[email_receives],
    )
    mail.mixed_subtype = 'related'
    mail.content_subtype = 'html'
    mail.attach_alternative(message, "text/html")
    mail.send()
