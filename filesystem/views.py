from rest_framework import generics
from .models import Directory, File
from .serializers import DirectorySerializer, FileSerializer



class DirectoryList(generics.ListCreateAPIView):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer


class DirectoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer


class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
