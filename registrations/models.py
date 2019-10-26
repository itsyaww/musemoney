from django.db import models

# Create your models here.
class Investor(models.Model):
    email = models.CharField()
    f_name = models.CharField() 
    l_name =models.CharField() 
    u_rname = models.CharField()
    capital = models.CharField()
class Artist(models.Model):
    email = models.CharField()
    f_name = models.CharField() 
    l_name =models.CharField() 
    u_rname = models.CharField()
    bio = models.CharField()
    twit_f = models.CharField()
    fb_f = models.CharField()
    yt_f = models.CharField()
    spotify_f = models.CharField()
    soundcloud_f = models.CharField()
    insta_f = models.CharField()
class asset(models.Model):
    
