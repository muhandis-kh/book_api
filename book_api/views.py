from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import AudioBook, Author, FileBook
from .serializers import AudioBookSerializer, AuthorSerializer, FileBookSerializer

# Create your views here.
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class FileBookViewset(viewsets.ModelViewSet):
    queryset = FileBook.objects.all()
    serializer_class = FileBookSerializer
    permission_classes = [AllowAny]
    
class AudioBookViewset(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    permission_classes = [AllowAny]
    
