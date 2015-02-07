from django.db import models

# Create your models here.
class Picture(models.Model):
	#things we need: location, time, date, text
	timestamp = models.DateTimeField(auto_now_add = True)
	text = models.TextField(max_length = 500, blank = True)
	image = models.ImageField()

	def __str__(self):
		return str(self.image) + ": " + str(self.text)

class Vote(models.Model):
	timestamp = models.DateTimeField(auto_now_add = True)
	picture = models.ForeignKey('Picture')

	def __str__(self):
		return str(self.picture.image) + ": " + str(self.picture.text)

class Winner(models.Model):
	date = models.DateField(editable = True)
	picture = models.OneToOneField('Picture')