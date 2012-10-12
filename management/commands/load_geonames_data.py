# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from cities.models import City, Region, Country
from dane_colombia.models import Departamento, Municipio
import unicodedata

def strip_accents(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

class Command(BaseCommand):

    help = "Carga las ciudades de la base de datos del DANE"



    def handle(self, *args, **options):

        colombia = Country.objects.get(name='Colombia')
        regions = Region.objects.filter(country=colombia, level=0)

        i = 0

        for region in regions:

            ciudades = City.objects.filter(region=region).order_by('name')

            for ciudad in ciudades:

                try:
                    d = Municipio.objects.get(nombre__iexact=strip_accents(ciudad.name), departamento__nombre__iexact=strip_accents(ciudad.region.name_std))
                    #d.location = ciudad.location
                    d.coords_long = ciudad.location.x
                    d.coords_lat = ciudad.location.y
                    d.save()
                except Municipio.DoesNotExist:

                    i += 1
                    print '- NO EXIST', ciudad, '*', strip_accents(ciudad.region.name_std)
                    d = Municipio.objects.filter(nombre__icontains=strip_accents(ciudad.name))
                    if d:
                        d = d[0]
                        #d.location = ciudad.location
                        d.coords_long = ciudad.location.x
                        d.coords_lat = ciudad.location.y
                        d.save()

                except Municipio.MultipleObjectsReturned:

                    #i += 1
                    print '* REPETIDO', ciudad
                    d = Municipio.objects.filter(nombre__iexact=strip_accents(ciudad.name))
                    print d


        print i

