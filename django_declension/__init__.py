from .models import Word
from lxml import etree
from urllib import urlencode
def declension(name):
  try:
    Word.objects.get(nominative = name)
  except Word.DoesNotExist:
    elements = etree.parse('http://export.yandex.ru/inflect.xml?' + urlencode({'name':name})).xpath('/inflections/inflection/text()')
    if elements:
      return Word.objects.create(
        nominative = name, 
        genitive = unicode(elements[1]),
        dative = unicode(elements[2]),
        accusative = unicode(elements[3]),
        instrumental = unicode(elements[4]),
        prepositional = unicode(elements[5]),
      )
    else:
      return None
