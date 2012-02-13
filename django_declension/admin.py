# -*- coding: utf-8 -*-

from django.contrib import admin

from django_declension.models import Word, DeclensionFail

admin.site.register(Word)
admin.site.register(DeclensionFail)
