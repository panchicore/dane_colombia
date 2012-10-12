# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Municipio.coords_lat'
        db.add_column('dane_colombia_municipio', 'coords_lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'Municipio.coords_long'
        db.add_column('dane_colombia_municipio', 'coords_long', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Municipio.coords_lat'
        db.delete_column('dane_colombia_municipio', 'coords_lat')

        # Deleting field 'Municipio.coords_long'
        db.delete_column('dane_colombia_municipio', 'coords_long')


    models = {
        'dane_colombia.departamento': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Departamento'},
            'codigo_dane': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'codigo_geonames': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'nombre'", 'overwrite': 'False', 'db_index': 'True'})
        },
        'dane_colombia.municipio': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Municipio'},
            'codigo_dane': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'coords_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coords_long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'municipios'", 'to': "orm['dane_colombia.Departamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'nombre'", 'overwrite': 'False', 'db_index': 'True'})
        }
    }

    complete_apps = ['dane_colombia']
