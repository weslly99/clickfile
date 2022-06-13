from .models import Directory, File
from rest_framework import serializers

class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ('id','name','parent','size','path','children_quantity','created_at','updated_at')
        read_only_fields = ('id', 'size','children_quantity','path','created_at','updated_at')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id','name','mime_type','size','content','directory','created_at','updated_at')
        read_only_fields = ('id','name','mime_type','size','created_at','updated_at')