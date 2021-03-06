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
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=310)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('paginaWeb', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('correoElectronico', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('rutaImagen', self.gf('django.db.models.fields.CharField')(max_length=310)),
            ('posicion', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('propietario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='propiedades', to=orm['auth.User'])),
        ))
        db.send_create_signal('publicidadGeolocalizada', ['PuntoDeInteres'])

        # Adding M2M table for field favoritos on 'PuntoDeInteres'
        db.create_table('publicidadGeolocalizada_puntodeinteres_favoritos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('puntodeinteres', models.ForeignKey(orm['publicidadGeolocalizada.puntodeinteres'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('publicidadGeolocalizada_puntodeinteres_favoritos', ['puntodeinteres_id', 'user_id'])

        # Adding model 'Anuncio'
        db.create_table('publicidadGeolocalizada_anuncio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anunciante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publicidadGeolocalizada.PuntoDeInteres'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('rutaImagen', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('publicidadGeolocalizada', ['Anuncio'])

        # Adding model 'Imagen'
        db.create_table('publicidadGeolocalizada_imagen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('publicidadGeolocalizada', ['Imagen'])


    def backwards(self, orm):
        # Deleting model 'PuntoDeInteres'
        db.delete_table('publicidadGeolocalizada_puntodeinteres')

        # Removing M2M table for field favoritos on 'PuntoDeInteres'
        db.delete_table('publicidadGeolocalizada_puntodeinteres_favoritos')

        # Deleting model 'Anuncio'
        db.delete_table('publicidadGeolocalizada_anuncio')

        # Deleting model 'Imagen'
        db.delete_table('publicidadGeolocalizada_imagen')


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
        'publicidadGeolocalizada.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'publicidadGeolocalizada.puntodeinteres': {
            'Meta': {'object_name': 'PuntoDeInteres'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'correoElectronico': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '310'}),
            'favoritos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favoritos'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'paginaWeb': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'posicion': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'propietario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'propiedades'", 'to': "orm['auth.User']"}),
            'rutaImagen': ('django.db.models.fields.CharField', [], {'max_length': '310'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['publicidadGeolocalizada']