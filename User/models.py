from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_birth = models.DateField(null=True, blank=True)

    
    GENDER_CHOICES = (('Ч', 'Чоловік'),('Ж', 'Жінка'),)
    	
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Ч')
    mailing = models.BooleanField(null =True)
    date_first_access = models.DateTimeField(default=timezone.now)
    date_last_access = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)