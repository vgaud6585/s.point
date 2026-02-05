from django.db import models

# Create your models here.
class StudyRecape(models.Model):
  heading = models.CharField(max_length=200)
  description = models.TextField()
  code_snippet = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.heading