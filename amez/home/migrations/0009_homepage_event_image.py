# Generated by Django 4.1.5 on 2023-02-01 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0008_homepage_about_us_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='event_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
