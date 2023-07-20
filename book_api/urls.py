from django.urls import path, include
from rest_framework import routers
from config import settings
from .views import FileBookViewset, AudioBookViewset, AuthorViewset, FileBookListView, AudioBookListView
from test import AddFiles

if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register('file-book-api', FileBookViewset)
router.register('audio-book-api', AudioBookViewset)
router.register('author-api', AuthorViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('files', FileBookListView.as_view(), name='files'),
    path('audios', AudioBookListView.as_view(), name='audios'),
    path('add-files', AddFiles, name='add-files'),
]