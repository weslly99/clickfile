from django.core.management.base import BaseCommand
from filesystem.models import Directory

class Command(BaseCommand):
    help = 'Remove a directory and all its contents'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=int, help='The directory pk')

    def handle(self, *args, **kwargs) -> None:
        directory_pk = kwargs['directory']
        directory = Directory.objects.get(pk = directory_pk)
        if directory:
            directory.delete()