# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Session.desc'
        db.delete_column(u'website_session', 'desc')


    def backwards(self, orm):
        # Adding field 'Session.desc'
        db.add_column(u'website_session', 'desc',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)


    models = {
        u'website.session': {
            'Meta': {'object_name': 'Session'},
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