from django.db import models

class Word(models.Model):
  nominative = models.CharField(max_length=255, unique = True)
  genitive = models.CharField(max_length=255)
  dative = models.CharField(max_length=255)
  accusative = models.CharField(max_length=255)
  instrumental = models.CharField(max_length=255)
  prepositional = models.CharField(max_length=255)
