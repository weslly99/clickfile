from filesystem.models import Directory, File
import pytest


@pytest.fixture
def directory(db):
    home = Directory.objects.create(name="Home",uri="home/")
    Directory.objects.create(name="Documents",uri="home/Documents", parent=home)
    return home


def test_directory_children_quantity(directory):
    assert directory.children_quantity == 1


def test_directory_size():
    pass
