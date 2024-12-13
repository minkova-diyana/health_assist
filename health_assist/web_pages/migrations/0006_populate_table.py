from django.db import migrations

from health_assist.web_pages.choices import TypeInsurance
from django.template.defaultfilters import slugify

def populate_table_information(apps, schema_editor):
    Pages = apps.get_model('web_pages', 'Pages')

    about = Pages.objects.create(name='about-us')
    news = Pages.objects.create(name='news')
    insurances = Pages.objects.create(name='insurances')

    Information = apps.get_model('web_pages', 'Information')
    data = [
        Information(
            title='Your insurance broker is an arm\'s length away',
            content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                    "the"
                    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
                    "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                    "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                    "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                    "and more recently with desktop p",
            hidden_info="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has "
                        "been the industry's standard dummy text ever since the 1500s, when an unknown printer took a "
                        "galley of type and scrambled it to make a type specimen book. It has survived not only five "
                        "centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
                        "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum "
                        "passages, and more recently with desktop p",
            pages=about,
            slug=slugify('Your insurance broker is an arm\'s length away')
        ),
        Information(
            title='News one',
            content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                    "the"
                    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
                    "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                    "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                    "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                    "and more recently with desktop p",
            hidden_info="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has "
                        "been the industry's standard dummy text ever since the 1500s, when an unknown printer took a "
                        "galley of type and scrambled it to make a type specimen book. It has survived not only five "
                        "centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
                        "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum "
                        "passages, and more recently with desktop p",
            pages=news,
            slug=slugify('News one')
        ),
        Information(
            title='News Two',
            content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                    "the"
                    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
                    "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                    "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                    "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                    "and more recently with desktop p",
            pages=news,
            slug=slugify('News Two')
        ),
        Information(
            title='Civil liability',
            content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                    "the"
                    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
                    "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                    "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                    "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                    "and more recently with desktop p",
            hidden_info="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has "
                        "been the industry's standard dummy text ever since the 1500s, when an unknown printer took a "
                        "galley of type and scrambled it to make a type specimen book. It has survived not only five "
                        "centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
                        "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum "
                        "passages, and more recently with desktop p",
            pages=insurances,
            type_insurance=TypeInsurance.GENERAL,
            slug=slugify('Civil liability')
        ),
        Information(
            title='Autocasco insurance',
            content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                    "the"
                    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
                    "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                    "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                    "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                    "and more recently with desktop p",
            hidden_info="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has "
                        "been the industry's standard dummy text ever since the 1500s, when an unknown printer took a "
                        "galley of type and scrambled it to make a type specimen book. It has survived not only five "
                        "centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
                        "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum "
                        "passages, and more recently with desktop p",
            pages=insurances,
            type_insurance=TypeInsurance.GENERAL,
            slug=slugify('Autocasco insurance')
        ),
        Information(
            title='Property insurance',
            content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                    "the"
                    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
                    "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                    "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                    "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                    "and more recently with desktop p",
            pages=insurances,
            type_insurance=TypeInsurance.GENERAL,
            slug=slugify('Property insurance')
        ),
        Information(
            title='Small Business',
            content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                    "the"
                    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
                    "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                    "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                    "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                    "and more recently with desktop p",
            hidden_info="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has "
                        "been the industry's standard dummy text ever since the 1500s, when an unknown printer took a "
                        "galley of type and scrambled it to make a type specimen book. It has survived not only five "
                        "centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
                        "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum "
                        "passages, and more recently with desktop p",
            pages=insurances,
            type_insurance=TypeInsurance.HEALTH,
            slug=slugify('Small Business')

        ),
        Information(
            title='Middle Buisneses',
            content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                    "the"
                    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
                    "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                    "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                    "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                    "and more recently with desktop p",
            pages=insurances,
            type_insurance=TypeInsurance.HEALTH,
            slug=slugify('Small Business2')

        ),
        Information(
            title='Big Buisneses',
            content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been "
                    "the"
                    "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type"
                    "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                    "but also the leap into electronic typesetting, remaining essentially unchanged. It was "
                    "popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, "
                    "and more recently with desktop p",
            hidden_info="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has "
                        "been the industry's standard dummy text ever since the 1500s, when an unknown printer took a "
                        "galley of type and scrambled it to make a type specimen book. It has survived not only five "
                        "centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
                        "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum "
                        "passages, and more recently with desktop p",
            pages=insurances,
            type_insurance=TypeInsurance.HEALTH,
            slug=slugify('Small Business3')
        ),
    ]
    Information.objects.bulk_create(data)

    Partners = apps.get_model('web_pages', 'Partners')
    p_data = [
        Partners(
            name='Bul Ins',
            image='partners/images_nICThzz.jpg',
            partner_url='https://www.bulins.com/'
        ),
        Partners(
            name='Armeec',
            image='partners/brand.gif',
            partner_url='https://www.armeec.bg/'
        ),
        Partners(
            name='Bulstrad',
            image='partners/bulstrad-vienna-insurance-group-vector-logo.png',
            partner_url='https://www.bulstrad.bg/'
        )
    ]

    Partners.objects.bulk_create(p_data)


class Migration(migrations.Migration):
    dependencies = [
        ('web_pages', '0005_alter_partners_image'),
    ]

    operations = [
        migrations.RunPython(populate_table_information)
    ]
