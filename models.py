from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Departamento(models.Model):
    """
    Departamentos de Colombia
    """
    nombre = models.CharField(_("Nombre del Departamento"), max_length=255)
    codigo_dane = models.CharField(_("Codigo DANE"), max_length=3) # No puede ser entero ya que tienen codigos como 05
    codigo_geonames = models.CharField(_("Codigo GeoNames"), max_length=10, null=True, blank=True)
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

    coords_lat = models.FloatField(null=True, blank=True)
    coords_long = models.FloatField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)

    class Meta:
        ordering = ("nombre",)

    def __unicode__(self):
        return '%s, %s' % ( self.nombre, self.departamento.nombre )

    def save(self, *args, **kwargs):
        if self.coords_lat:
            print self.coords_lat
            point = Point(self.coords_long, self.coords_lat)
            print point
            self.location = point
        super(Municipio, self).save(*args, **kwargs)
