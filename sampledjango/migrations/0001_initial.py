# Generated by Django 2.2 on 2019-07-10 17:14

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndeedJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_created=True, auto_now_add=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('salary', models.CharField(blank=True, max_length=200, null=True)),
                ('job_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('date_posted', models.CharField(blank=True, max_length=200, null=True)),
                ('job_url', models.URLField(blank=True, max_length=1000, null=True, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
