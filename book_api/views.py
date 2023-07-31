
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from book_api.api.permissions import IsAdminUserOrReadOnly
from .models import AudioBook, Author, FileBook
from .serializers import AudioBookSerializer, AuthorSerializer, FileBookSerializer
    
class FileBookViewset(viewsets.ModelViewSet):
    queryset = FileBook.objects.all()
    serializer_class = FileBookSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['@document_filename', '@description']
    
class AudioBookViewset(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['@document_filename', '@description']

    
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]