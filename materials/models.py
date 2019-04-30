from django.db import models
from django.contrib.contenttypes.models import ContentType
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


	# def save(self):
 #        super().save()
 #        img = Image.open(self.image.path)
 #        if img.height > 300 or img.width > 300:
 #            output_size = (300, 300)
 #            img.thumbnail(output_size)
 #            img.save(self.image.path)

