from django.urls import path, include
from rest_framework import routers
from config import settings
from .views import FileBookViewset, AudioBookViewset, AuthorViewset, UserRegistrationView
from tests.test import AddFiles, AddAudios
from data.data import ADD_FILES_LINK, ADD_AUDIOS_LINK

if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register('file-book-api', FileBookViewset)
router.register('audio-book-api', AudioBookViewset)
router.register('author-api', AuthorViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path(ADD_FILES_LINK, AddFiles, name='add-files'),
    path(ADD_AUDIOS_LINK, AddAudios, name='add-audios'),
]