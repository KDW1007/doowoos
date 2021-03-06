# Generated by Django 4.0.2 on 2022-02-16 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_alter_playlist_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cover', models.FileField(null=True, upload_to='')),
                ('create_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AddField(
            model_name='playlist',
            name='playlist_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='create_date',
            field=models.DateTimeField(null=True),
        ),
    ]
