from django.db import models

# Create your models here.
class Task(models.Model):
    
    TASK_SIZE = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )
    
    title = models.CharField(max_length = 100, null=False, blank=False)    
    details = models.TextField(max_length = 300, null=False, blank=False)    
    date_added = models.DateTimeField(auto_now_add = True)    
    completed = models.BooleanField()
    size = models.CharField(max_length = 100, null=False, blank=False, choices=TASK_SIZE)        
    
    objects = models.Manager()        

    def __unicode__(self):
        return self.title
            