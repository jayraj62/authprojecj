# Generated by Django 4.0.4 on 2022-06-16 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxapp', '0002_notesdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phnno', models.BigIntegerField()),
                ('name', models.TextField()),
            ],
        ),
    ]