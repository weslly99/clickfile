from django.db.models import Sum
from django.utils.functional import cached_property
from django.db import models
from .mixins import TimestampableMixin
from . import services


class Directory(TimestampableMixin, models.Model):
    """Represents the Directories and subdirectories"""

    name = models.CharField(max_length=200)
    path = models.URLField(max_length=255, unique=True, db_index=True)
    parent = models.ForeignKey(
        "filesystem.Directory",
        related_name="children_directories",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    @cached_property
    def children_quantity(self):
        directories = self.children_directories.count()
        files = self.children_files.count()
        return directories + files

    @cached_property
    def size(self) -> float:

        total = 0.0
        for direcotry in self.children_directories.all():
            if direcotry.size is not None:
                total += direcotry.size
        total_file = self.children_files.aggregate(total=Sum("size"))["total"]
        if total_file is not None:
            total += total_file
        return round(total, 2)

    def __str__(self):
        return f"{self.path}"

    def save(self, *args, **kwargs):
        base_path = ''
        if self.parent:
            base_path = self.parent.path
        self.path = "".join([base_path, '/', self.name])
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("name", "updated_at")
        verbose_name_plural = "Directories"


class File(TimestampableMixin, models.Model):
    """Represents the files"""
    
    name = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=50)
    uri = models.URLField(max_length=255)
    size = models.FloatField(default=0)
    content = models.FileField(upload_to="media/files/%Y/%m/%d")
    directory = models.ForeignKey(
        "filesystem.Directory",
        related_name="children_files",
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        if self.id is None:
            self.name = self.content.name
            self.mime_type = services.get_mime_type(self.content.name)
            self.size = services.convert_size_to_mb_decimal(self.content.size)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("name", "updated_at")
        verbose_name_plural = "Files"

    def __str__(self):
        return self.name
