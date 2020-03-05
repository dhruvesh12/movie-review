from django.db import models

# Create your models here.
class category(models.Model):
	ids=models.IntegerField(default=0)
	name=models.CharField(max_length=100,null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name


class movie(models.Model):
	movie_ids=models.IntegerField(default=0,blank=True)
	movie_name=models.CharField(max_length=200,blank=True)
	movie_lang=models.CharField(max_length=200,blank=True)
	movie_desc=models.TextField(null=True)
	status=models.CharField(max_length=100,blank=True)
	movie_logo=models.CharField(max_length=200,null=True)
	movie_vote=models.FloatField(null=True, blank=True, default=None)
	movie_pop=models.FloatField(null=True, blank=True, default=None)
	categorys=models.ManyToManyField(category,blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.movie_name



class lists(models.Model):
	list_name=models.CharField(max_length=100,null=True)
	list_movie=models.ManyToManyField(movie,blank=True)

	def __str__(self):
		return self.list_name