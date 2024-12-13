from django.db import migrations
from health_assist.accounts.models import InsuredCompanies
from health_assist.packages.models import Documents, Packages, CompanyPackages, UnderPackages


def populate_existing_companies_data(apps, schema_editor):
    # Get the existing InsuredCompanies records based on a unique field (e.g., name)
    try:
        company1 = InsuredCompanies.objects.get(name="KPMG")
        company2 = InsuredCompanies.objects.get(name="HEETS")
    except InsuredCompanies.DoesNotExist:
        raise ValueError("One or more InsuredCompanies not found.")

    # Populate Documents
    document1 = Documents.objects.create(type_document="Invoice")
    document2 = Documents.objects.create(type_document="Claim Form")
    document3 = Documents.objects.create(type_document="Prescription")
    document4 = Documents.objects.create(type_document="Fiscal receipt corresponding with the invoice")

    # Populate Packages
    package1 = Packages.objects.create(name="Outpatient medical careee")
    package2 = Packages.objects.create(name="Inpatient medical careee")
    package3 = Packages.objects.create(name="Dental medical care ")

    # Create individual CompanyPackages instances for each package
    CompanyPackages.objects.create(company=company1, packages=package1)
    CompanyPackages.objects.create(company=company1, packages=package2)
    CompanyPackages.objects.create(company=company2, packages=package1)
    CompanyPackages.objects.create(company=company2, packages=package2)
    CompanyPackages.objects.create(company=company2, packages=package3)

    # Create UnderPackages instances
    under_package1 = UnderPackages(
        packages=package1,
        company=company1,  # Ensure this is the actual instance of InsuredCompanies
        name="Basic Coverage A",
        limit="10000 USD",
        coverage="General medical coverage for basic health."
    )

    under_package2 = UnderPackages(
        packages=package1,
        company=company1,  # Ensure this is the actual instance of InsuredCompanies
        name="Basic Coverage B",
        limit="10000 USD",
        coverage="General medical coverage for basic health."
    )

    under_package3 = UnderPackages(
        packages=package2,
        company=company2,  # Ensure this is the actual instance of InsuredCompanies
        name="Premium Coverage A",
        limit="50000 USD",
        coverage="Extensive medical coverage for premium health."
    )

    under_package4 = UnderPackages(
        packages=package2,
        company=company2,  # Ensure this is the actual instance of InsuredCompanies
        name="Premium Coverage B",
        limit="50000 USD",
        coverage="Extensive medical coverage for premium health."
    )

    # Save the instances to ensure they are stored in the database
    under_package1.save()
    under_package2.save()
    under_package3.save()
    under_package4.save()

    # Now link the ManyToManyField `documents_needed` to the created `Documents` instances
    under_package1.documents_needed.add(document1, document2, document3)
    under_package2.documents_needed.add(document1, document2, document3, document4)
    under_package3.documents_needed.add(document1, document2, document3)
    under_package4.documents_needed.add(document1, document2, document3, document4)


class Migration(migrations.Migration):
    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_existing_companies_data),
    ]
