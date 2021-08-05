# Generated by Django 3.2.5 on 2021-08-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=300)),
                ('post_date', models.DateTimeField()),
                ('post_text', models.CharField(max_length=300)),
                ('post_image', models.ImageField(upload_to='post_image/')),
            ],
        ),
    ]
