import os, csv
from django.core.management.base import BaseCommand
from dane_colombia.models import Departamento, Municipio

class Command(BaseCommand):
    help = "Carga las ciudades de la base de datos del DANE"

    def handle(self, *args, **options):
        PROJECT_DIR = os.path.dirname(__file__)
        PATH = os.path.join(PROJECT_DIR, '..', '..', 'data', 'ciudades.csv')
        print 'Guardando...'
        with open(PATH, 'rb') as csv_ciudades_dane:
            lineas = csv.reader(csv_ciudades_dane, delimiter=';')
            header = lineas.next()
            for linea in lineas:
                codigo_departamento = linea[0]
                nombre_departamento = linea[1]
                codigo_municipio = linea[2]
                nombre_municipio = linea[3]
                departamento, creado = Departamento.objects.get_or_create(nombre=nombre_departamento, codigo_dane=codigo_departamento)
                ciudad, creado = Municipio.objects.get_or_create(nombre=nombre_municipio, codigo_dane=codigo_municipio, departamento=departamento)
        print 'Listo.'