from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class ContentList(models.Model):
    ContentId = models.AutoField(primary_key=True)
    BlockName = models.CharField(max_length=20, null=True)
    Title = models.CharField(max_length=150, null=True, blank=True)
    Content = models.CharField(max_length=500, null=True, blank=True)
    ImgPath = models.ImageField(upload_to='image/', blank=True, null=True)
    Alt = models.CharField(max_length=20, null=True, blank=True)
    CreateDate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.Title

class TDKList(models.Model):
    Title = models.CharField(max_length=50, null=True)
    Description = models.CharField(max_length=150, null=True, blank=True)
    Keywords = models.CharField(max_length=50, null=True, blank=True)