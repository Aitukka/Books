# Generated by Django 5.0.6 on 2024-06-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_rating_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Баға беру жұлдызы', 'verbose_name_plural': 'Баға беру жұлдыздары'},
        ),
        migrations.AddField(
            model_name='book',
            name='book_file',
            field=models.FileField(blank=True, null=True, upload_to='book_files/', verbose_name='Файл кітап'),
        ),
    ]
