# Generated by Django 4.0.2 on 2022-02-16 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cover', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.FileField(null=True, upload_to='')),
                ('book_title', models.CharField(max_length=100)),
                ('intro', models.TextField(null=True)),
                ('upload_date', models.DateTimeField(null=True)),
                ('book_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('books_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.books')),
                ('chapter_title', models.CharField(max_length=100)),
                ('views', models.IntegerField(null=True)),
                ('contents', models.TextField(null=True)),
                ('reading_time', models.IntegerField(null=True)),
                ('chapter_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
            bases=('books.books',),
        ),
    ]
