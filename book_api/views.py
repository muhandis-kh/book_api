from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters
from .models import AudioBook, Author, FileBook
from .serializers import AudioBookSerializer, AuthorSerializer, FileBookSerializer
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer

# Create your views here.
class FileBookListView(ListAPIView):
    queryset = FileBook.objects.all()
    serializer_class = FileBookSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    filter_backends = [filters.SearchFilter]
    search_fields = ['@document_filename', '@description']
    
class AudioBookListView(ListAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['@document_filename', '@description']
    
class FileBookViewset(viewsets.ModelViewSet):
    queryset = FileBook.objects.all()
    serializer_class = FileBookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=document_filename', '$description']
    
class AudioBookViewset(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=document_filename', '@description']

    
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]