import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="iso_code",
            field=models.CharField(
                max_length=3, validators=[django.core.validators.MinLengthValidator(3)]
            ),
        ),
    ]
