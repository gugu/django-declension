# -*- coding: utf-8 -*-

from django import template

from django_declension import declension

register = template.Library()

@register.filter(name='declension')
def declension_filter(name, inflection):
    word = declension(name)
    inflected_word = getattr(word, inflection, name)

    return inflected_word
