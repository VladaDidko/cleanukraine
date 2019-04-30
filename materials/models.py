from django.db import models
from PIL import Image

class Type(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Code(models.Model):
	type_code = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
	code = models.IntegerField(primary_key=True)
	abbreviation = models.CharField(max_length=20)
	description = models.TextField()
	image = models.ImageField(default='default.jpg', upload_to='material_pics')


	def __str__(self):
		return self.abbreviation

class Waste(models.Model):
	code = models.ForeignKey(Code, on_delete = models.DO_NOTHING)
	id_waste = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=100)
	description = models.TextField()
	utilization = models.TextField()
	image = models.ImageField(default="default", upload_to='material_pics')

	def __str__(self):
		return self.title

