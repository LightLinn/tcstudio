from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class BlogList (models.Model):
    BlogId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50, null=True)
    Catego = models.CharField(max_length=10, null=True, blank=True)
    Tag = models.CharField(max_length=50, null=True, blank=True)
    Desc = models.CharField(max_length=150, null=True, blank=True)
    Author = models.CharField(max_length=20, null=True, blank=True)
    Content = RichTextField(null=True, blank=True)
    PubTime = models.DateTimeField(auto_now=True)
    Enable = models.BooleanField(default=False)
    Press = models.IntegerField(default=0)
    Like = models.IntegerField(default=0)

    def __str__(self):
        return self.Title

