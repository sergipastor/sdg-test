import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_country_iso_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="iso_code",
            field=models.CharField(
                max_length=3,
                unique=True,
                validators=[django.core.validators.MinLengthValidator(3)],
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
