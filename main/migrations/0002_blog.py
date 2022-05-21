# Generated by Django 4.0.4 on 2022-05-20 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog_desc', models.TextField()),
                ('blog_writer', models.CharField(max_length=100)),
            ],
        ),
    ]