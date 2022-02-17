from django.db import models
from django.utils import timezone

# Create your models here.

class PrimerModelo(models.Model):
    campo_uno = models.CharField(max_length=255, null=False)
    edad = models.IntegerField(null=False)
    create = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    # class Meta:
    #     db_table = 'primer_modelo'

class SegundoModelo(models.Model):
    campo_uno = models.CharField(max_length=255, null=True)
    edad = models.IntegerField(null=True, default=0)
    create = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    class Meta:
        db_table = 'segundo_modelo'