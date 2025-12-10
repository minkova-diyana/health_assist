from django.core.mail import send_mail
from django.dispatch import Signal, receiver
from health_assist import settings

contact_form_submitted = Signal()


@receiver(contact_form_submitted)
def send_email(sender, **kwargs):
    name = kwargs.get('name')
    email = kwargs.get('email')
    subject = kwargs.get('subject')
    message = kwargs.get('message')

    full_message = f"Message from {name} ({email}):\n\n{message}"

    try:
        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,    # from
            [settings.EMAIL_HOST_USER],  # to
            fail_silently=False
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
