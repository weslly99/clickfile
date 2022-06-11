from django.utils.functional import cached_property
from django.db import models
from .mixins import TimestampableMixin


class Directory(TimestampableMixin, models.Model):
    name = models.CharField(max_length=200)
    uri = models.URLField(max_length=255)
    size = models.IntegerField(default=0)
    parent = models.ForeignKey(
        "filesystem.Directory",
        related_name="children",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("name", "updated_at")

    @cached_property
    def children_quantity(self):
        return self.children.count()


class File(TimestampableMixin, models.Model):
    name = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=50)
    uri = models.URLField(max_length=255)
    size = models.IntegerField(default=0)
    directory = models.ForeignKey(
        "filesystem.Directory", verbose_name="directory", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("name", "updated_at")
