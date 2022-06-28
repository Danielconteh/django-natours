from django.db import models
from django.contrib.auth.models import User


# Create your models here.

LEVEL_CHECK = [
    ('difficulty', 'difficulty'),
    ('easy', 'easy'),
    ('medium', 'medium'),
]


# THE LOCATION MODEL THAT CONNECT WITH -> TOUR MODEL
class Location(models.Model):
    description = models.CharField(blank=True, null=True,max_length=100)
    address = models.CharField(blank=True, null=True,max_length=150)
    coordinates = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name_plural = 'location'




# THE TOUR MODEL

class Tour(models.Model):
    ratingAvg = models.DecimalField(blank=True, null=True,max_digits=5,decimal_places=1)
    ratingQuantity = models.IntegerField(blank=True, null=True)
    startDates = models.JSONField(blank=True, null=True)
    name = models.CharField(blank=True, null=True,max_length=100)
    slug = models.SlugField(unique=True)
    duration = models.IntegerField(blank=True, null=True)
    maxGroupSize = models.IntegerField(blank=True, null=True)
    difficulty = models.CharField(max_length=10,choices=LEVEL_CHECK)
    price = models.IntegerField(blank=True, null=True)
    summary = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    coverImage = models.FileField(upload_to='cover_img/',blank=True, null=True)
    location = models.JSONField(blank=True, null=True)
    startLocation = models.ForeignKey(Location,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'tour'
 
 
 
 # THE Images MODEL THAT CONNECT WITH -> TOUR MODEL
 
class Images(models.Model):
    post = models.ForeignKey(Tour, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'tours_img/')
    
    class Meta:
        verbose_name_plural = 'images'



class User_Image(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo =  models.ImageField(upload_to = 'Users', null=True, blank=True)
    image = models.URLField(max_length=1000, null=True, blank=True)

# , default=""







# POST REVIEW DATA class EmailField(max_length=254, **options)¶

class Review(models.Model):
    tour = models.SlugField(max_length=200,blank=True,null=True)
    user = models.EmailField(blank=True,null=True)
    review = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=5, blank=True, decimal_places=1, null=True)
    time_posted = models.TextField(blank=True, null=True)
    
    class Meta:
        unique_together = ('tour', 'user',)
    


# WORKING API KEY => SECRET
# client_id = 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
# secret_key = 1045610393790-67euil14f1nc9acfdcn38i86lo9toegf.apps.googleusercontent.com






