from django.db import models

class ArtistManager(models.Manager):

    def get_query_set(self):
        return super(ArtistManager, self).get_query_set().filter(published=True)