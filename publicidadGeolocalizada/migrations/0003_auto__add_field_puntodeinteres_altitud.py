# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PuntoDeInteres.altitud'
        db.add_column('publicidadGeolocalizada_puntodeinteres', 'altitud',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PuntoDeInteres.altitud'
        db.delete_column('publicidadGeolocalizada_puntodeinteres', 'altitud')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'publicidadGeolocalizada.anuncio': {
            'Meta': {'object_name': 'Anuncio'},
            'anunciante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publicidadGeolocalizada.PuntoDeInteres']"}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rutaImagen': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '180'})
        },
        'publicidadGeolocalizada.puntodeinteres': {
            'Meta': {'object_name': 'PuntoDeInteres'},
            'altitud': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'correoElectronico': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '310'}),
            'favoritos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favoritos'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'paginaWeb': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'posicion': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'pripietario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'propiedades'", 'to': "orm['auth.User']"}),
            'rutaImagen': ('django.db.models.fields.CharField', [], {'max_length': '310'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['publicidadGeolocalizada']