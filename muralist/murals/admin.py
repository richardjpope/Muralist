from models import *
from django.contrib import admin

# Murals
class MuralColourInline(admin.TabularInline):
    model = MuralColour
    extra = 10

class MuralEventInline(admin.TabularInline):
    model = MuralEvent

class MuralMaterialInline(admin.TabularInline):
    model = MuralMaterial

class MuralAlternativeNameInline(admin.TabularInline):
    model = MuralAlternativeName    

class MuralBuildingAttributeInline(admin.TabularInline):
    model = MuralBuildingAttribute
    
class MuralFunderInline(admin.TabularInline):
    model = MuralFunder
    
class MuralAdmin(admin.ModelAdmin):
    prepopulated_fields = {"uri_slug": ("title",)}
    inlines = [
          MuralColourInline,
          MuralEventInline,
          MuralMaterialInline,
          MuralAlternativeNameInline,          
          MuralBuildingAttributeInline,
          MuralFunderInline,
      ]

# Artists
class ArtistEducationInline(admin.TabularInline):
    model = ArtistEducation

class ArtistNonMuralWorkInline(admin.TabularInline):
    model = ArtistNonMuralWork
    
class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"uri_slug": ("name",)}
    inlines = [
        ArtistEducationInline,
        ArtistNonMuralWorkInline, 
      ]

# Memories
class MemoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"uri_slug": ("title",)}

# Workshops
class WorkshopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"uri_slug": ("name",)}
        
# Memories
class MemoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"uri_slug": ("title",)}    
    
admin.site.register(Mural, MuralAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Memory, MemoryAdmin)
