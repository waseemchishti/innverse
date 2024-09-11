from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='uploads/blog/')
    description = models.TextField()
    title2 = models.CharField(max_length=250, blank=True )
    description2 = models.TextField(default='', blank=True, null=True)
    title3 = models.CharField(max_length=250, blank=True )
    description3 = models.TextField(default='', blank=True, null=True)
    point1 = models.CharField(max_length=250, blank=True, null=True )
    des1 = models.TextField(default='', blank=True, null=True)
    point2 = models.CharField(max_length=250, blank=True, null=True )
    des2 = models.TextField(default='', blank=True, null=True)
    point3 = models.CharField(max_length=250, blank=True, null=True )
    des3 = models.TextField(default='', blank=True, null=True)
    point4 = models.CharField(max_length=250, blank=True, null=True )
    des4 = models.TextField(default='', blank=True, null=True)   
    point5 = models.CharField(max_length=250, blank=True, null=True )
    des5 = models.TextField(default='', blank=True, null=True)  
    point6 = models.CharField(max_length=250, blank=True, null=True )
    des6 = models.TextField(default='', blank=True, null=True)  
    point7 = models.CharField(max_length=250, blank=True, null=True )
    des7 = models.TextField(default='', blank=True, null=True)  
    point8 = models.CharField(max_length=250, blank=True, null=True )
    des8 = models.TextField(default='', blank=True, null=True)
    point9 = models.CharField(max_length=250, blank=True, null=True )
    des9 = models.TextField(default='', blank=True, null=True) 
    point10 = models.CharField(max_length=250, blank=True, null=True )
    des10 = models.TextField(default='', blank=True, null=True)  
    bolg_date = models.DateField()  # For storing the date
    blog_time = models.TimeField()  # For storing the time
    blog_writer = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title 