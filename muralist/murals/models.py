from django.db import models
import managers.mural
import managers.artist

# Artists
class Artist(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length = 100, null=False, blank=False, verbose_name='Artist name')
    short_biography = models.TextField(max_length = 300, null=True, blank=True)
    long_biography = models.TextField(null=True, blank=True)    
    date_added = models.DateTimeField(auto_now_add = True, verbose_name='Date artist was added to this database')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Date of birth')
    date_of_death = models.DateField(null=True, blank=True, verbose_name='Date of death')
    place_of_birth = models.CharField(max_length = 100, null=True, blank=True, verbose_name='Place of birth')
    lat_of_birth = models.FloatField(null=True, blank=True, verbose_name='Latitude of birth place')
    lng_of_birth = models.FloatField(null=True, blank=True, verbose_name='Longitude of birth')
    url = models.URLField(verify_exists=True, max_length=200, null=True, blank=True, verbose_name='URL for Website belonging to the artist')
    wikipedia_uri = models.URLField(verify_exists=True, max_length=200, null=True, blank=True, verbose_name='URL for Wikipedia page for the artist')
    notes = models.TextField(max_length = 300, null=True, blank=True, verbose_name='Research notes', help_text="These do not get published")    
    uri_slug = models.SlugField()
    published = models.BooleanField(help_text='show or hide this item on the website')    

    objects = models.Manager()
    published_objects = managers.artist.ArtistManager()
    
    def __unicode__(self):
        return self.name

class ArtistEducation(models.Model):
    class Meta:
        verbose_name_plural = "Artist's Education"
        ordering = ['start_date']
        
    artist = models.ForeignKey(Artist)
    institution_name = models.CharField(max_length = 100, null=False, blank=False)
    course_name = models.CharField(max_length = 100, null=True, blank=True)    
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    notes = models.TextField(max_length = 300, null=True, blank=True, verbose_name='Research notes', help_text="These do not get published")

    def __unicode__(self):
        return self.institution_name + ' - ' + self.course_name

class ArtistNonMuralWork(models.Model):
    class Meta:
        verbose_name_plural = "Artist's Non-mural works"
        ordering = ['date']
        
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length = 100, null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    notes = models.TextField(max_length = 300, null=True, blank=True, verbose_name='Research notes', help_text="These do not get published")    

    def __unicode__(self):
        return self.title

# Groups
class Workshop(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length = 100, null=False, blank=False, verbose_name='Name of the group')    
    short_description = models.TextField(max_length = 300, null=True, blank=True, help_text="keep this short and concise")    
    long_description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    artists = models.ManyToManyField(Artist, null=True, blank=True)    
    date_added = models.DateTimeField(auto_now_add = True, verbose_name='Date workshop was added to this database')    
    notes = models.TextField(max_length = 300, null=True, blank=True, verbose_name='Research notes', help_text="These do not get published")    
    uri_slug = models.SlugField()
    published = models.BooleanField(help_text='show or hide this item on the website')            
    has_header_image = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

# Murals
class Mural(models.Model):
    class Meta:
        ordering = ['title']

    CONDITION_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),)

    title = models.CharField(max_length = 100, null=False, blank=False, verbose_name='Primary name of mural')
    short_description = models.TextField(max_length = 300, null=True, blank=True, help_text="keep this short and concise")
    long_description = models.TextField(null=True, blank=True)
    locality = models.CharField(max_length = 255, null=True, blank=True, help_text='how you would describe it to someone in conversation e.g. Hackney or Wandsworth')    
    address = models.CharField(max_length = 255, null=False, blank=False, verbose_name='Address of the mural')
    location_description = models.TextField(max_length = 255, null=False, blank=False, verbose_name='How to find it', help_text="explain where to stand and look to find the mural")
    lat = models.FloatField(null=False, blank=False, verbose_name='Latitude of mural', help_text="as a decimal number")
    lng = models.FloatField(null=False, blank=False, verbose_name='Longitude of mural', help_text="as a decimal number")
    width = models.IntegerField(null=True, blank=True, verbose_name='Width of the mural', help_text="in meters")
    height = models.IntegerField(null=True, blank=True, verbose_name='Height of the mural in meters', help_text="in meters")
    date_added = models.DateTimeField(auto_now_add = True, verbose_name='Date mural was added to this database')
    date_completed = models.DateField(null=True, blank=True, verbose_name='Date the mural was completed', help_text="this also needs adding to the 'events' section")
    wikipedia_uri = models.URLField(verify_exists=True, max_length=200, null=True, blank=True, verbose_name='URL for Wikipedia page for the mural')
    lost = models.BooleanField(help_text='This mural was no longer exists')    
    condition_rank = models.IntegerField(null=True, blank=True, verbose_name='Condition 1-10', help_text='1-3 is in danger, 4-7 is ok, 8-10 is good', choices = CONDITION_CHOICES)
    condition_description = models.TextField(max_length = 300, null=True, blank=True, verbose_name='Description of the condition / state of repair')    
    published = models.BooleanField(help_text='show or hide this item on the website')        
    notes = models.TextField(max_length = 300, null=True, blank=True, verbose_name='Research notes', help_text="These do not get published")    
    nearest_underground = models.CharField(max_length = 100, null=True, blank=True, help_text='Name of one or more tubes stations')
    nearest_railway_station = models.CharField(max_length = 100, null=True, blank=True, help_text='Name of one or more railway stations')    
    bus_routes = models.CharField(max_length = 100, null=True, blank=True, help_text='Name of one or more bus routes separated by commas')
    uri_slug = models.SlugField()
    artists = models.ManyToManyField(Artist, blank=True, null=True)
    

    objects = models.Manager()
    published_objects = managers.mural.MuralManager()

    def __unicode__(self):
        return self.title

    def condition_text(self):
        result = 'is in good condition'         
        if self.lost:
            result = 'has been lost'
        elif self.condition_rank <= 3:
            result = 'is under threat'
        elif self.condition_rank <= 7:
            result = 'is in OK condition'
        return result

    def condition_tag(self):
        result = 'good'
        if self.lost:
            result = 'lost'
        elif self.condition_rank <= 3:
            result = 'threat'
        elif self.condition_rank <= 7:
            result = 'ok'

        return result

    def event_years(self):
        years = []
        events = self.muralevent_set.all()        
        year = int(events[0].date.year)       
        end_year = events[len(events) -1].date.year
        while (year <= end_year):
            years.append(year)
            year = year + 1
        return years  

class MuralAlternativeName(models.Model):
    class Meta:
        ordering = ['name']
        
    mural = models.ForeignKey(Mural)
    name = models.CharField(max_length = 100, null=False, blank=False, verbose_name='An alternative name')

    def __unicode__(self):
        return self.name
    
class MuralFunder(models.Model):
    class Meta:
        ordering = ['name']
        
    mural = models.ForeignKey(Mural)
    name = models.CharField(max_length = 100, null=False, blank=False, verbose_name='Name of funder')
    uri = models.URLField(verify_exists=True, max_length=200, null=True, blank=True, verbose_name='URL for funder', help_text="e.g. a wikipedia article or their webpage")    
    notes = models.TextField(max_length = 300, null=True, blank=True, verbose_name='Research notes', help_text="These do not get published")    
    
    def __unicode__(self):
        return self.name

class MuralEvent(models.Model):
    class Meta:
        ordering = ['date']
        
    mural = models.ForeignKey(Mural)    
    title = models.CharField(max_length = 100, null=False, blank=False, verbose_name='Title for the event')    
    date = models.DateField(null=True, blank=True, verbose_name='Date of the event')
    fuzzy = models.BooleanField(verbose_name='Fuzzy date, e.g. only year known')
    description = models.TextField(max_length = 300, null=True, blank=True,verbose_name='Short description')    
    
    def __unicode__(self):
        return self.title

class MuralColour(models.Model):
    mural = models.ForeignKey(Mural)
    hex_value = models.CharField(max_length = 6, null=False, blank=False, verbose_name='Hex colour value')
    
    def __unicode__(self):
        return self.hex_value

class MuralBuildingAttribute(models.Model):
    BUILDING_CHOICES = (
        ('status', 'Status'),
        ('type', 'Type'),
        ('period', 'Period'),
        ('condition', 'Condition'),
        ('ownership', 'Ownership'),
        ('other', 'Other'),
    )
    mural = models.ForeignKey(Mural)
    attribute_type = models.CharField(max_length = 100, null=False, blank=False, choices=BUILDING_CHOICES)    
    attribute_value = models.CharField(max_length = 100, null=False, blank=False)    
    description = models.TextField(max_length = 300, null=True, blank=True,verbose_name='Short description')    

    def __unicode__(self):
        return self.attribute_value
        
class MuralMaterial(models.Model):
    
    MATERIAL_CHOICES = (
        ('paint', 'Paint'),
        ('tile', 'Tile'),
        ('other', 'Other'),        
    )

    mural = models.ForeignKey(Mural)
    material_type = models.CharField(max_length = 100, null=False, blank=False, choices=MATERIAL_CHOICES)
    material_value = models.CharField(max_length = 100, null=False, blank=False)

    def __unicode__(self):
        return self.material_value
        
# Memories
class Memory(models.Model):
    class Meta:
               verbose_name_plural = "Memories"

    MEDIA_CHOICES = (
        ('text', 'Text'),
        ('youtube', 'Video (YouTube.com)'),
        ('audioboo', 'Audio (AudioBoo.com)'),
    )
    title = models.CharField(max_length = 100, null=False, blank=False, verbose_name='Title for this memory')
    short_description = models.TextField(max_length = 300, null=False, blank=False,verbose_name='Short description')
    media_type = models.CharField(max_length = 100, null=False, blank=False, choices=MEDIA_CHOICES)
    mural = models.ForeignKey(Mural)    
    date_added = models.DateTimeField(auto_now_add = True, verbose_name='Date memory was added to this database')
    person_name = models.CharField(max_length = 100, null=False, blank=False, help_text="Name of the person interviewed / filmed")
    person_description = models.CharField(max_length = 100, null=True, blank=True, help_text="e.g. Brixton resident / artist")
    date_of_interview = models.DateField(null=False, blank=False)
    uri = models.URLField(verify_exists=True, max_length=200, null=True, blank=True, verbose_name='URL for video or audio', help_text="YouTube or AudioBoo web page")
    memory_text = models.TextField(null=True, blank=True, help_text="Only use this for a written memory")
    notes = models.TextField(max_length = 300, null=True, blank=True, verbose_name='Research notes', help_text="These do not get published")        
    published = models.BooleanField(help_text='show or hide this item on the website')
    uri_slug = models.SlugField()
    
    def __unicode__(self):
        return self.title