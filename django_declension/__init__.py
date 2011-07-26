from .models import Word
from lxml import etree
from urllib import urlencode

def declension(name):
  try:
    return Word.objects.get(nominative = name)
  except Word.DoesNotExist:
    elements = etree.parse('http://export.yandex.ru/inflect.xml?' + urlencode(
      {
        'name':name.encode('utf-8')
      }
    )).xpath('/inflections/inflection/text()')
    if len(elements)>1:
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
