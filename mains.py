
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class User(models.Model):

    nickname = models.CharField(
        max_length=100,
        unique=True,
    )

    profile_image = models.ImageField(upload_to='/avatars/')
    password = models.TextField()


class Publication(models.Model):
    image = models.ImageField(upload_to='/publication_images/')
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')


class PublicationComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    comment = models.TextField()



class LikeUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('user', 'product')
