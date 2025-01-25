from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_country_iso_code_alter_country_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
