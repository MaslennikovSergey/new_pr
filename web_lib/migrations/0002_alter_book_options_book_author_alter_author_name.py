# Generated by Django 4.1.5 on 2023-01-04 19:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_lib', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'get_latest_by': 'published', 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='web_lib.author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Wrong', regex='^.*em$')], verbose_name='Имя автора'),
        ),
    ]
