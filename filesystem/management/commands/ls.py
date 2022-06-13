from django.core.management.base import BaseCommand
from filesystem.models import Directory

class Command(BaseCommand):
    help = 'list all files and subdirectories in a directory'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=int, help='The directory pk')

    def handle(self, *args, **kwargs) -> None:
        """List all files and Directories in the directory"""
        directory_pk = kwargs['directory']
        directory = Directory.objects.get(pk = directory_pk)
        subdirectories = list(directory.children_directories.all())
        files = list(directory.children_files.all())
        children = list(subdirectories + files)
        names = ["".join([child.name, '\n']) for child in children]
        self.stdout.write("".join(names))