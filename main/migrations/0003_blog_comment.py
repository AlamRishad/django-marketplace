# Generated by Django 4.0.4 on 2022-05-21 10:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_writer', models.CharField(max_length=100)),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_desc', models.TextField()),
                ('blog_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.blog')),
            ],
        ),
    ]
