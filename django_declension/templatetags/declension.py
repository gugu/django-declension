from django_declension import declension
from django import template

register = template.Library()

@register.filter(name='declension')
def declension_filter(name, inflection):
    word = declension(name)
    try:
        inflected_word = getattr(word, inflection)
    except AttributeError:
        inflected_word = name

    return inflected_word
