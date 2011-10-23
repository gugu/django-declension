from django_declension import declension
from django import template

register = template.Library()

@register.filter(name='declension')
def declension_filter(name, inflection):
    word = declension(name)
    return getattr(word, inflection)
