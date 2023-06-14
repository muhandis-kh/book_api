from rest_framework import serializers
from .models import FileBook, Author, AudioBook

class FileBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileBook
        fields = ('__all__')
   
class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ('__all__')
     
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')