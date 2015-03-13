from django.db import models
from django.forms import ModelForm
from time import time

# Create your models here.

# uploading files
def get_upload_file_name(instance, filename):
	return "%s_%s" % (str(time()).replace('.','_'),filename)
	
class kicks(models.Model):
	kickTitle = models.CharField(max_length = 30)
	releaseDate = models.CharField(max_length = 15)
	category = models.CharField(max_length = 30)
	directors = models.CharField(max_length = 75)
	writers = models.CharField(max_length = 75)
	stars = models.CharField(max_length = 90)
	ratings = models.CharField(max_length = 30)
	links = models.CharField(max_length = 200)
	poster = models.FileField(upload_to=get_upload_file_name)


class users(models.Model):
	userName = models.CharField(max_length = 30)
	firstName = models.CharField(max_length = 30)
	lastName = models.CharField(max_length = 30)
	email = models.CharField(max_length = 40)
	expertise = models.CharField(max_length = 75)
	genres = models.CharField(max_length = 120)
	ratings = models.CharField(max_length = 200)
	top100 = models.CharField(max_length = 200)
	watchlist = models.CharField(max_length = 200)	
	thumbnail = models.FileField(upload_to=get_upload_file_name)



class edit_profile_form(ModelForm):
	class Meta:
		model = users
		fields = ['firstName','lastName','email','expertise','genres','ratings','top100','watchlist', 'thumbnail']

class add_kick_form(ModelForm):
	class Meta:
		model = kicks
		fields = ['kickTitle','releaseDate','category','directors','writers','stars','ratings','links', 'poster']