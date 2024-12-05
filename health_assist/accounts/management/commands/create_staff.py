from django.core.management.base import BaseCommand

from health_assist.accounts.models import HnfUserModel


class Command(BaseCommand):
    help = "Create a staff user"

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help="The email of the staff user")
        parser.add_argument('password', type=str, help="The password for the staff user")

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']

        try:
            user = HnfUserModel.objects.create_staff(
                email=email,
                password=password,
            )
            self.stdout.write(self.style.SUCCESS(f"Staff user {email} created successfully!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error creating staff user: {e}"))
