# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Session'
        db.create_table(u'website_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'website', ['Session'])

        # Adding model 'Speaker'
        db.create_table(u'website_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(related_name='speakers', to=orm['website.Session'])),
        ))
        db.send_create_signal(u'website', ['Speaker'])


    def backwards(self, orm):
        # Deleting model 'Session'
        db.delete_table(u'website_session')

        # Deleting model 'Speaker'
        db.delete_table(u'website_speaker')


    models = {
        u'website.session': {
            'Meta': {'object_name': 'Session'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'website.speaker': {
            'Meta': {'object_name': 'Speaker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'speakers'", 'to': u"orm['website.Session']"})
        }
    }

    complete_apps = ['website']