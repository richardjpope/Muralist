from django.db import models

class MuralManager(models.Manager):

    def get_query_set(self):
        return super(MuralManager, self).get_query_set().filter(published=True)