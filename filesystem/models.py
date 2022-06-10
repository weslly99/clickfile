from django.db import models


class Directory(models.Model):
    name = models.CharField(max_length=200)
    uri = models.URLField(max_length=255)
    size = models.IntegerField()
    parent = models.ForeignKey("filesystem.Directory", verbose_name="parent", on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)