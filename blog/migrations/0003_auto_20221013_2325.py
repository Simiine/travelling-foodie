# Generated by Django 3.2.16 on 2022-10-13 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221011_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='recipe',
            field=models.TextField(),
        ),
    ]
