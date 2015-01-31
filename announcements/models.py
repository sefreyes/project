from django.db import models

# Create your models here.

class Announcements_list(models.Model):
	a_list=[]

class Announcement_node(models.Model):
	announcement_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

