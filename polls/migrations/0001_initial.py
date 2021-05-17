# Generated by Django 3.2.3 on 2021-05-17 10:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('date_published', models.DateTimeField(default=datetime.datetime(2021, 5, 17, 13, 59, 19, 189113), verbose_name='Дата публикации')),
                ('is_active', models.BooleanField(verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, verbose_name='Ответ')),
                ('votes', models.IntegerField(default=0, verbose_name='Голосов')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
