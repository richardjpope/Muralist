# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Mural.bus_routes'
        db.add_column('murals_mural', 'bus_routes', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Mural.nearest_underground'
        db.add_column('murals_mural', 'nearest_underground', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Mural.nearest_railway_station'
        db.add_column('murals_mural', 'nearest_railway_station', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Mural.bus_routes'
        db.delete_column('murals_mural', 'bus_routes')

        # Deleting field 'Mural.nearest_underground'
        db.delete_column('murals_mural', 'nearest_underground')

        # Deleting field 'Mural.nearest_railway_station'
        db.delete_column('murals_mural', 'nearest_railway_station')
    
    
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
            'bus_routes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'nearest_railway_station': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nearest_underground': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
    
    complete_apps = ['murals']
