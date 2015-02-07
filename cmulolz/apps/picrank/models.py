from django.db import models

# Create your models here.
class Picture(models.Model):
	#things we need: location, time, date, text
	timestamp = models.DateTimeField(auto_now_add = True)
	text = models.TextField(max_length = 500, blank = True)
	image = models.ImageField()

class Vote(models.Model):
	timestamp = models.DateTimeField(auto_now_add = True)
	picture = models.ForeignKey('Picture')