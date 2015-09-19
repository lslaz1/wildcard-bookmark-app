from django.db import models

class Bookmark(models.Model):
	URL = models.TextField()
	Description = models.TextField()
