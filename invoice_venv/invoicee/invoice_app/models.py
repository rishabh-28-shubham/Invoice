from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User

# declaring a client models
class Client(models.Model):
    #basic fileds
    clientName = models.CharField(null=True, blank=True, max_lenght=200)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_lenght=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return ''
    

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('=')[4]
            self.slug = slugify('')

        self.slug = slugify('')
        self.last_update = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)