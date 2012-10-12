El Departamento Administrativo Nacional de Estadística (DANE),  es la entidad responsable de la planeación, levantamiento, procesamiento, análisis y difusión de las estadísticas oficiales de Colombia.
Esta es una aplicación escrita en Python para el framework Django para facilitar a developers tener información geografica y estadistica de Colombia.

---

Cobertura del proyecto:

1. Base de Datos de ciudades de Colombia con lenguaje estandar del DANE (Listo).

TODO:

2. Relacionar con datos de GeoNames. (Listo, faltan algunas coordenadas)
3. Agregar soporte GeoDjango (postgis) para las ciudades y departamentos (Listo).
4. Conectar estadisticas.

Autor:

@panchicore

---

REQUIERE:
- geodjango, DATABASES.ENGINE: 'django.contrib.gis.db.backends.postgis'
- django_extensions