from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField

class Departamento(models.Model):
    """
    Departamentos de Colombia
    """
    nombre = models.CharField(_("Nombre del Departamento"), max_length=255)
    codigo_dane = models.CharField(_("Codigo DANE"), max_length=3) # No puede ser entero ya que tienen codigos como 05
    slug = AutoSlugField(populate_from='nombre')

    class Meta:
        ordering = ("nombre",)

    def __unicode__(self):
        return self.nombre

class Municipio(models.Model):
    """
    Ciudades de Colombia
    """
    departamento = models.ForeignKey(Departamento, related_name='municipios', verbose_name=_("Departamento"))
    nombre = models.CharField(_("Nombre del Municipio"), max_length=255)
    codigo_dane = models.CharField(_("Codigo DANE"), max_length=3)
    slug = AutoSlugField(populate_from='nombre')

    class Meta:
        ordering = ("nombre",)

    def __unicode__(self):
        return self.nombre
