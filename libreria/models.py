from contextlib import nullcontext
from django.db import models

# Create your models here.
class Book(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to='images/', verbose_name='Image', null=True)
  description = models.TextField(null=True, verbose_name='Description')

  def __str__(self):
    row = "Title: " + self.title + " - Description: " + self.description
    return row

  #Boorar la imagen fisicamente.
  def delete(self, using=None, keep_parents=False):
    self.image.storage.delete(self.image.name)
    super().delete()

