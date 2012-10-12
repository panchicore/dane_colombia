# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Departamento'
        db.create_table('dane_colombia_departamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codigo_dane', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='nombre', overwrite=False, db_index=True)),
        ))
        db.send_create_signal('dane_colombia', ['Departamento'])

        # Adding model 'Municipio'
        db.create_table('dane_colombia_municipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codigo_dane', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='nombre', overwrite=False, db_index=True)),
        ))
        db.send_create_signal('dane_colombia', ['Municipio'])


    def backwards(self, orm):
        
        # Deleting model 'Departamento'
        db.delete_table('dane_colombia_departamento')

        # Deleting model 'Municipio'
        db.delete_table('dane_colombia_municipio')


    models = {
        'dane_colombia.departamento': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Departamento'},
            'codigo_dane': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'nombre'", 'overwrite': 'False', 'db_index': 'True'})
        },
        'dane_colombia.municipio': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Municipio'},
            'codigo_dane': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'nombre'", 'overwrite': 'False', 'db_index': 'True'})
        }
    }

    complete_apps = ['dane_colombia']
