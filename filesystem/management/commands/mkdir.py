from django.core.management.base import BaseCommand
from filesystem.models import Directory

class Command(BaseCommand):
    help = 'Create a directory'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='The name of the directory to be created')
        parser.add_argument('parent', type=int, help='The parent directory pk')

    def handle(self, *args, **kwargs) -> None:
        name = kwargs['name']
        parent = kwargs['parent']
        Directory.objects.create(name=name, parent_id=parent)