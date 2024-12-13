from django.core.mail import send_mail
from django.dispatch import Signal, receiver
from asgiref.sync import sync_to_async
from health_assist import settings

contact_form_submitted = Signal()


async def send_email_async(subject, message, recipient_list, from_email=None):
    await sync_to_async(send_mail)(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )


@receiver(contact_form_submitted)
def send_email(sender, **kwargs):
    name = kwargs.get('name')
    email = kwargs.get('email')  # Sender email (entered in the form)
    subject = kwargs.get('subject')  # Email subject
    message = kwargs.get('message')  # Email message

    full_message = f"Message from {name} ({email}):\n\n{message}"

    try:
        import asyncio
        asyncio.run(
            send_email_async(
                subject,
                full_message,
                [settings.EMAIL_HOST_USER],
                email,
            )
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
