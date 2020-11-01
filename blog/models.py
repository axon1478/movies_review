import random
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from tinymce import HTMLField


class Movies(models.Model):
    advt = models.ImageField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    series = models.BooleanField(default=False)
    by = models.CharField(max_length=100)
    imdb = models.FloatField(default=8, max_length=10)
    rotten_tomatoes = models.PositiveIntegerField(default=89, max_length=100)
    date_released = models.DateTimeField(null=True, blank=True)
    date_modify = models.DateTimeField(default=timezone.now)
    description = HTMLField(blank=True, null=True)

    movies_stream = models.CharField(max_length=30000, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    image_link = models.CharField(max_length=30000, blank=True, null=True)

    num_of_sessions = models.IntegerField(default=5)
    num_of_episodes = models.IntegerField(default=20)

    action = models.BooleanField(default=False)
    sifi = models.BooleanField(default=False)
    thriller = models.BooleanField(default=False)
    adventure = models.BooleanField(default=False)
    classic = models.BooleanField(default=False)
    Romance = models.BooleanField(default=False)
    animation = models.BooleanField(default=False)
    drama = models.BooleanField(default=False)
    crime = models.BooleanField(default=False)
    mystery = models.BooleanField(default=False)
    family = models.BooleanField(default=False)
    documentary = models.BooleanField(default=False)
    fantasy = models.BooleanField(default=False)
    comedy = models.BooleanField(default=False)

    ep1 = models.CharField(max_length=30000, blank=True, null=True)
    ep2 = models.CharField(max_length=30000, blank=True, null=True)
    ep3 = models.CharField(max_length=30000, blank=True, null=True)
    ep4 = models.CharField(max_length=30000, blank=True, null=True)
    ep5 = models.CharField(max_length=30000, blank=True, null=True)
    ep6 = models.CharField(max_length=30000, blank=True, null=True)
    ep7 = models.CharField(max_length=30000, blank=True, null=True)
    ep8 = models.CharField(max_length=30000, blank=True, null=True)
    ep9 = models.CharField(max_length=30000, blank=True, null=True)
    ep10 = models.CharField(max_length=30000, blank=True, null=True)
    ep11 = models.CharField(max_length=30000, blank=True, null=True)
    ep12 = models.CharField(max_length=30000, blank=True, null=True)
    ep13 = models.CharField(max_length=30000, blank=True, null=True)
    ep14 = models.CharField(max_length=30000, blank=True, null=True)
    ep15 = models.CharField(max_length=30000, blank=True, null=True)
    ep16 = models.CharField(max_length=30000, blank=True, null=True)
    ep17 = models.CharField(max_length=30000, blank=True, null=True)
    ep18 = models.CharField(max_length=30000, blank=True, null=True)
    ep19 = models.CharField(max_length=30000, blank=True, null=True)
    ep20 = models.CharField(max_length=30000, blank=True, null=True)
    ep21 = models.CharField(max_length=30000, blank=True, null=True)
    ep22 = models.CharField(max_length=30000, blank=True, null=True)
    ep23 = models.CharField(max_length=30000, blank=True, null=True)
    ep24 = models.CharField(max_length=30000, blank=True, null=True)
    ep25 = models.CharField(max_length=30000, blank=True, null=True)
    ep26 = models.CharField(max_length=30000, blank=True, null=True)
    ep27 = models.CharField(max_length=30000, blank=True, null=True)
    ep28 = models.CharField(max_length=30000, blank=True, null=True)
    ep29 = models.CharField(max_length=30000, blank=True, null=True)
    ep30 = models.CharField(max_length=30000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Movie"

    def __str__(self):
        return self.name


def get_id():
    return


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Movies, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    # return reverse('post-detail' , kwargs={'pk':self.pk})


class Sliders(models.Model):
    image = models.ImageField()
    number = models.IntegerField()


class Advt(models.Model):
    advt = models.ImageField()
