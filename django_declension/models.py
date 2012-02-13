# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Word(models.Model):
    nominative = models.CharField(_("Nominative"), max_length=255, unique = True)
    genitive = models.CharField(_("Genitive"), max_length=255)
    dative = models.CharField(_("Dative"), max_length=255)
    accusative = models.CharField(_("Accusative"), max_length=255)
    instrumental = models.CharField(_("Instrumental"), max_length=255)
    prepositional = models.CharField(_("Prepositional"), max_length=255)

    def __unicode__(self):
        return self.nominative

    class Meta:
        verbose_name = _("Word")
        verbose_name_plural = _("Words")


class DeclensionFail(models.Model):
    word = models.CharField(_("Word"), max_length=255, unique = True)

    def __unicode__(self):
        return self.word

    class Meta:
        verbose_name = _("Declension Fail")
        verbose_name_plural = _("Declension Fails")
