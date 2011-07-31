from .models import Word
from lxml import etree
from urllib import urlencode
from urllib2 import urlopen

def declension(name):
    try:
        return Word.objects.get(nominative = name)
    except Word.DoesNotExist:
        try:
            elements = etree.parse(urlopen('http://export.yandex.ru/inflect.xml?' + urlencode(
              {
                'name':name.encode('utf-8')
              }
            ), timeout = 2)).xpath('/inflections/inflection/text()')
        except IOError:
            # These *** banned us, so we will silently return nothing
            # When ban will be over we can use it again
            return None
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
            # TODO: Store unsuccessfull responses
            return None
