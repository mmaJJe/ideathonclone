import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    main_title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    contents = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(
        null = True,
        blank = True,
        upload_to = "postImg"
    )

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super(Image, self).delete(*args, **kargs)