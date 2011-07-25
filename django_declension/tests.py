# vim: set fileencoding=utf8 :
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django_declension import declension

class DeclTest(TestCase):
    def test_basic_declension(self):
        self.assertEqual(declension('упячка').genitive,u'упячки');
