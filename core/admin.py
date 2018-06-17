# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ('question_text','pub_date')
    list_display = ('question_text','pub_date')
    list_filter = ('pub_date',)


admin.site.register(Question,QuestionAdmin)