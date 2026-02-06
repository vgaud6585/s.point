from django.db import models

# Create your models here.
class Clips(models.Model):
	heading = models.CharField(max_length = 90)
	code_clip = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.heading