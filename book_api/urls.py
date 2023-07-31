from django.urls import path, include
from rest_framework import routers
from config import settings
from .views import FileBookViewset, AudioBookViewset, AuthorViewset
from test import AddFiles
from data.data import ADD_FILES_LINK

if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register('file-book-api', FileBookViewset)
router.register('audio-book-api', AudioBookViewset)
router.register('author-api', AuthorViewset)
urlpatterns = [
    path('', include(router.urls)),
    path(ADD_FILES_LINK, AddFiles, name='add-files'),
]