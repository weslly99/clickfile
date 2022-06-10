from django.db import models
from .mixins import TimestampableMixin


class Directory(TimestampableMixin, models.Model):
    name = models.CharField(max_length=200)
    uri = models.URLField(max_length=255)
    size = models.IntegerField()
    parent = models.ForeignKey("filesystem.Directory", verbose_name="parent", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('name','updated_at')


class File(TimestampableMixin, models.Model):
    name = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=50)
    uri = models.URLField(max_length=255)
    size = models.IntegerField()
    directory = models.ForeignKey("filesystem.Directory", verbose_name="directory", on_delete=models.CASCADE)

    class Meta:
        ordering = ('name','updated_at')
