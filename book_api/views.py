
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from book_api.api.permissions import IsAdminUserOrReadOnly
from .models import AudioBook, Author, FileBook
from .serializers import AudioBookSerializer, AuthorSerializer, FileBookSerializer, UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from .renderers import UserRenderer
from book_api.api.throttles import CustomUserRateThrottle, CustomBearerTokenRateThrottle
from book_api.api.filters import CustomStatusFilter

class FileBookViewset(viewsets.ModelViewSet):
    queryset = FileBook.objects.all()
    serializer_class = FileBookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [filters.SearchFilter, CustomStatusFilter]
    search_fields = ['@document_filename', '@description', '@slug']
    throttle_classes  = [CustomBearerTokenRateThrottle]
    
class AudioBookViewset(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [filters.SearchFilter, CustomStatusFilter]
    search_fields = ['@document_filename', '@description', '@slug']
    throttle_classes  = [CustomBearerTokenRateThrottle]
    
class FileBookAPIView(ListAPIView):
    queryset = FileBook.objects.all()
    serializer_class = FileBookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['@document_filename', '@description']
    throttle_classes  = [CustomBearerTokenRateThrottle]
    
class AudioBookAPIView(ListAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['@document_filename', '@description']
    throttle_classes  = [CustomUserRateThrottle]

    
class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]
    
""" Authentification Views """
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token': token, 'message': "Ro'yhatdan muvaffaqiyatli o'tdingiz"}, status=HTTP_201_CREATED)
