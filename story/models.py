from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User

class Story(models.Model):
	title = models.CharField(max_length=75)
	body = models.TextField()
	author = models.ForeignKey(User,null=True)
	pub_date = models.DateTimeField(default=timezone.now)
	total_votes = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Vote(models.Model):
	story = models.ForeignKey(Story,null=True)
	voter = models.ForeignKey(User,null=True)
	has_voted = models.BooleanField(default=False)
	vote_cast = models.IntegerField(default=0)