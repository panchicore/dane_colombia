# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Departamento.codigo_geonames'
        db.add_column('dane_colombia_departamento', 'codigo_geonames', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Departamento.codigo_geonames'
        db.delete_column('dane_colombia_departamento', 'codigo_geonames')


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
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'municipios'", 'to': "orm['dane_colombia.Departamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'nombre'", 'overwrite': 'False', 'db_index': 'True'})
        }
    }

    complete_apps = ['dane_colombia']
