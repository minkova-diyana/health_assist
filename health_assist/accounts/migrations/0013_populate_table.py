from datetime import date

from django.db import migrations


def populate_employee_company(apps, schema_editor):
    Company = apps.get_model('accounts', 'InsuredCompanies')

    c_1 = Company.objects.create(
        name='KPMG',
        insurance_company_name='Bg-Insurance',
        contract_start_date=date(2023, 1, 1),
        contract_end_date=date(2025, 1, 1)
    )
    c_2 = Company.objects.create(
        name='HEETS',
        insurance_company_name='Bg-Insurance',
        contract_start_date=date(2024, 6, 15),
        contract_end_date=date(2026, 6, 15)
    )

    Employee = apps.get_model('accounts', 'EmployeeProfile')

    data = [
        Employee(
            first_name='Gosho',
            last_name='Peshov',
            uc_id_num='9805024659',
            company=c_1
        ),
        Employee(
            first_name='Ginka',
            last_name='Mirova',
            uc_id_num='8810028459',
            company=c_2
        )
    ]

    Employee.objects.bulk_create(data)


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0012_alter_hnfusermodel_uc_id_number'),
    ]

    operations = [
        migrations.RunPython(populate_employee_company),

    ]
