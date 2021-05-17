# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import *


class AnswerInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'is_active']}
         ),
        ('Информация о дате',
         {'fields': ['date_published'],
          'classes': ['collapse']}
         ),
    ]
    inlines = [AnswerInline]
    list_display = ('title', 'date_published', 'is_active', 'is_popular')
    search_fields = ['title']
    list_filter = ['date_published']


admin.site.register(Question, QuestionAdmin)
# Register your models here.
