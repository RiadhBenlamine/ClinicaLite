from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import Group, Permission
from core.models import Clinic

class Command(BaseCommand):
    help = 'Setting up ClinicaLite'

    def add_arguments(self, parser):
        parser.add_argument('clinic_name', type=str, help='Clinic name')
        parser.add_argument('phone', type=str, help='Clinic phone number')
        parser.add_argument('email', type=str, help='Clinic email address')

    @transaction.atomic
    def handle(self, *args, **options):

        clinic_name = options['clinic_name']
        phone = options['phone']
        email = options['email']


        # Check if clinic already exists
        if Clinic.objects.exists():
            self.stdout.write(self.style.WARNING("Clinic already initialized. Aborting."))
            return

        # Create clinic entry
        clinic = Clinic.objects.create(
            name=clinic_name,
            phone=phone,
            email=email,
        )

        for group_name in "Doctors", "Receptionist":
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' created."))
            else:
                self.stdout.write(self.style.WARNING(f"Group '{group_name}' already exists."))

        self.stdout.write(self.style.SUCCESS(f"Clinic '{clinic.name}' created."))
        self.stdout.write(self.style.SUCCESS("ClinicaLite setup completed successfully."))
        self.stdout.write(self.style.NOTICE("Now create superuser using: python manage.py createsuperuser"))