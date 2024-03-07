from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User

# declaring a client models
class Client(models.Model):

    # Making PROVINCES
    PROVINCES = [
        ('Gauteng', 'Gauteng'),
        ('Free State', 'Free State'),
        ('Limpopo', 'Limpopo'),
    ]

    #basic fileds
    clientName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    province = models.CharField(choices=PROVINCES, blank=True, max_length=100)
    postalCode =  models.CharField(null=True, blank=True, max_length=10)
    phoneNumber =  models.CharField(null=True, blank=True, max_length=100)
    emailAddress =  models.CharField(null=True, blank=True, max_length=100)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.province ,self.uniqueId)
    

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('=')[4]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.province ,self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.province ,self.uniqueId))
        self.last_update = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)



# product & services model 
class Product(models.Model):
    CURRENCY = [
        ('₹','INR'),
        ('R','ZAR'),
    ]

    #basic fileds 
    title = models.CharField(null=True, blank=True, max_length=100)
    discription = models.TextField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default ='₹', max_length=100)


    #utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True,  blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)
    
    def get_absolute_rul(self):
        return reverse('product-detail', kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        
        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Product, self).save(*args,**kwargs)

        

#Invoice Models
class Invoice(models.Model):
    TERMS =[
        ('14 days','14 days'),
        ('30 days','30 days'),
        ('60 days','60 days'),
        ('90 days','90 days'),
    ]

    STATUS = [
        ('CURRNET','CURRENT'),
        ('OVERDUE','OVERDUE'),
        ('PAID','PAID'),
    ]


    #basic fileds --> Invoice Model
    title = models.CharField(null=True, blank=True, max_length=100)
    number = models.CharField(null=True, blank=True, max_length=100)
    dueDate = models.DateField(null=True, blank=True)
    paymentTerms = models.CharField(choices=TERMS, default='14 days', max_length=100)
    status = models.CharField(choices=STATUS,  default='CURRENT', max_length=100)
    notes = models.TextField(null=True, blank=True)

    #accessing clinet and product model
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)


    #utility filelds
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)



    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)
    
    def get_absolute_rul(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        
        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Invoice, self).save(*args,**kwargs)