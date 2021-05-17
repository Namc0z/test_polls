# -*- coding:utf-8 -*-

import datetime
from django.db import models
from core import settings


class Question(models.Model):
    """Вопрос"""
    title = models.CharField(max_length=200, verbose_name="Вопрос")
    date_published = models.DateTimeField(verbose_name="Дата публикации",
                                          default=datetime.datetime.now())
    is_active = models.BooleanField(verbose_name="Опубликован : ")

    def __unicode__(self):
        return self.title

    def is_popular(self):
        answers = Choice.objects.filter(question_id=self.id)
        votes_total = sum([answer.votes for answer in answers])
        return votes_total > settings.POLLS_POPULAR_VOTES_LIMIT

    # Описание столбца в админке
    is_popular.short_description = 'Популярный'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    """Ответы пользователей"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name="Ответ", max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


# Create your models here.
