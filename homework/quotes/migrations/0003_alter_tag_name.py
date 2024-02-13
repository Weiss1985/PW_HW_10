from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_rename_desvription_author_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
