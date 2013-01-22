# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PuntoDeInteres'
        db.create_table('publicidadGeolocalizada_puntodeinteres', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('paginaWeb', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('correoElectronico', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('rutaImagen', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('posicion', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('publicidadGeolocalizada', ['PuntoDeInteres'])

        # Adding model 'Anuncio'
        db.create_table('publicidadGeolocalizada_anuncio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('rutaImagen', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('propietario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publicidadGeolocalizada.PuntoDeInteres'])),
        ))
        db.send_create_signal('publicidadGeolocalizada', ['Anuncio'])


    def backwards(self, orm):
        # Deleting model 'PuntoDeInteres'
        db.delete_table('publicidadGeolocalizada_puntodeinteres')

        # Deleting model 'Anuncio'
        db.delete_table('publicidadGeolocalizada_anuncio')


    models = {
        'publicidadGeolocalizada.anuncio': {
            'Meta': {'object_name': 'Anuncio'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propietario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publicidadGeolocalizada.PuntoDeInteres']"}),
            'rutaImagen': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'publicidadGeolocalizada.puntodeinteres': {
            'Meta': {'object_name': 'PuntoDeInteres'},
            'correoElectronico': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'paginaWeb': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'posicion': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'rutaImagen': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['publicidadGeolocalizada']