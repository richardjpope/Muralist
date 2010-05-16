# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
  
class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Artist'
        db.create_table('murals_artist', (
            ('short_biography', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('long_biography', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('lat_of_birth', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lng_of_birth', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('date_of_death', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('uri_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('wikipedia_uri', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('place_of_birth', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('muralist', ['Artist'])

        # Adding model 'ArtistEducation'
        db.create_table('murals_artisteducation', (
            ('course_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['murals.Artist'])),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('institution_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('muralist', ['ArtistEducation'])

        # Adding model 'ArtistNonMuralWork'
        db.create_table('murals_artistnonmuralwork', (
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['murals.Artist'])),
        ))
        db.send_create_signal('muralist', ['ArtistNonMuralWork'])

        # Adding model 'Workshop'
        db.create_table('murals_workshop', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('uri_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('long_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('muralist', ['Workshop'])

        # Adding M2M table for field artists on 'Workshop'
        db.create_table('murals_workshop_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workshop', models.ForeignKey(orm['murals.workshop'], null=False)),
            ('artist', models.ForeignKey(orm['murals.artist'], null=False))
        ))
        db.create_unique('murals_workshop_artists', ['workshop_id', 'artist_id'])

        # Adding model 'Mural'
        db.create_table('murals_mural', (
            ('date_completed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('wikipedia_uri', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uri_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('location_description', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('condition_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_description', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('long_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('condition_description', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal('muralist', ['Mural'])

        # Adding M2M table for field artists on 'Mural'
        db.create_table('murals_mural_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mural', models.ForeignKey(orm['murals.mural'], null=False)),
            ('artist', models.ForeignKey(orm['murals.artist'], null=False))
        ))
        db.create_unique('murals_mural_artists', ['mural_id', 'artist_id'])

        # Adding model 'MuralAlternativeName'
        db.create_table('murals_muralalternativename', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mural', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['murals.Mural'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('muralist', ['MuralAlternativeName'])

        # Adding model 'MuralFunder'
        db.create_table('murals_muralfunder', (
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mural', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['murals.Mural'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('muralist', ['MuralFunder'])

        # Adding model 'MuralEvent'
        db.create_table('murals_muralevent', (
            ('description', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mural', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['murals.Mural'])),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fuzzy', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('muralist', ['MuralEvent'])

        # Adding model 'MuralColour'
        db.create_table('murals_muralcolour', (
            ('hex_value', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mural', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['murals.Mural'])),
        ))
        db.send_create_signal('muralist', ['MuralColour'])

        # Adding model 'MuralBuildingAttribute'
        db.create_table('murals_muralbuildingattribute', (
            ('attribute_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mural', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['murals.Mural'])),
            ('attribute_value', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('muralist', ['MuralBuildingAttribute'])

        # Adding model 'MuralMaterial'
        db.create_table('murals_muralmaterial', (
            ('material_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mural', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['murals.Mural'])),
            ('material_value', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('muralist', ['MuralMaterial'])

        # Adding model 'Memory'
        db.create_table('murals_memory', (
            ('person_description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('person_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('memory_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('mural', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['murals.Mural'])),
            ('uri_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('date_of_interview', self.gf('django.db.models.fields.DateField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('media_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('muralist', ['Memory'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Artist'
        db.delete_table('murals_artist')

        # Deleting model 'ArtistEducation'
        db.delete_table('murals_artisteducation')

        # Deleting model 'ArtistNonMuralWork'
        db.delete_table('murals_artistnonmuralwork')

        # Deleting model 'Workshop'
        db.delete_table('murals_workshop')

        # Removing M2M table for field artists on 'Workshop'
        db.delete_table('murals_workshop_artists')

        # Deleting model 'Mural'
        db.delete_table('murals_mural')

        # Removing M2M table for field artists on 'Mural'
        db.delete_table('murals_mural_artists')

        # Deleting model 'MuralAlternativeName'
        db.delete_table('murals_muralalternativename')

        # Deleting model 'MuralFunder'
        db.delete_table('murals_muralfunder')

        # Deleting model 'MuralEvent'
        db.delete_table('murals_muralevent')

        # Deleting model 'MuralColour'
        db.delete_table('murals_muralcolour')

        # Deleting model 'MuralBuildingAttribute'
        db.delete_table('murals_muralbuildingattribute')

        # Deleting model 'MuralMaterial'
        db.delete_table('murals_muralmaterial')

        # Deleting model 'Memory'
        db.delete_table('murals_memory')
    
    
    models = {
        'murals.artist': {
            'Meta': {'object_name': 'Artist'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_death': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat_of_birth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng_of_birth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'long_biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'short_biography': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'uri_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wikipedia_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'murals.artisteducation': {
            'Meta': {'object_name': 'ArtistEducation'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['murals.Artist']"}),
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'murals.artistnonmuralwork': {
            'Meta': {'object_name': 'ArtistNonMuralWork'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['murals.Artist']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'murals.memory': {
            'Meta': {'object_name': 'Memory'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_interview': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'memory_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mural': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['murals.Mural']"}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'person_description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'uri_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'murals.mural': {
            'Meta': {'object_name': 'Mural'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['murals.Artist']", 'null': 'True', 'blank': 'True'}),
            'condition_description': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'condition_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_completed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'location_description': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'long_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uri_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wikipedia_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'murals.muralalternativename': {
            'Meta': {'object_name': 'MuralAlternativeName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mural': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['murals.Mural']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'murals.muralbuildingattribute': {
            'Meta': {'object_name': 'MuralBuildingAttribute'},
            'attribute_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'attribute_value': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mural': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['murals.Mural']"})
        },
        'murals.muralcolour': {
            'Meta': {'object_name': 'MuralColour'},
            'hex_value': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mural': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['murals.Mural']"})
        },
        'murals.muralevent': {
            'Meta': {'object_name': 'MuralEvent'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'fuzzy': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mural': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['murals.Mural']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'murals.muralfunder': {
            'Meta': {'object_name': 'MuralFunder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mural': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['murals.Mural']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'murals.muralmaterial': {
            'Meta': {'object_name': 'MuralMaterial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'material_value': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mural': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['murals.Mural']"})
        },
        'murals.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['murals.Artist']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'uri_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['muralist']
