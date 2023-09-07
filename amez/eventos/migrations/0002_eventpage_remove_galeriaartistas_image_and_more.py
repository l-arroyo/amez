# Generated by Django 4.1.5 on 2023-09-07 13:06

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('informacion', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='galeriaartistas',
            name='image',
        ),
        migrations.RemoveField(
            model_name='galeriaartistas',
            name='page',
        ),
        migrations.DeleteModel(
            name='Eventos',
        ),
        migrations.DeleteModel(
            name='GaleriaArtistas',
        ),
    ]
