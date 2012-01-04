from .models import Word, DeclensionFail
from lxml import etree
from urllib import urlencode
from urllib2 import urlopen
from django.core.cache import cache

def declension(name):
    try:
        declension = cache.get('declension|' + name.replace(' ','|'))
        if declension is None:
            if cache.get('declensionfail|' + name.replace(' ','|')):
                return None
            elif DeclensionFail.objects.filter(word=name).count():
                cache.set('declensionfail|' + name.replace(' ','|'), True)
                return None
            declension = Word.objects.get(nominative = name)
        cache.set('declension|' + name.replace(' ','|'), declension)
        return declension
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
            DeclensionFail.objects.create(word=name)
            return None
