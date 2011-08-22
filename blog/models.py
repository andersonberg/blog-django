from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey(User)
	date = models.DateField()
	title = models.CharField(max_length=100)
	post = models.TextField()
