# Generated by Django 4.2.1 on 2023-06-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0007_alter_filebook_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='audio_book_author'),
        ),
    ]
