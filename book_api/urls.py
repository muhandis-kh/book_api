from django.urls import path, include
from rest_framework import routers
from .views import FileBookViewset, AudioBookViewset, AuthorViewset

router = routers.DefaultRouter()

router.register('file-book-api', FileBookViewset)
router.register('audio-book-api', AudioBookViewset)
router.register('author-api', AuthorViewset)
urlpatterns = [
    path('', include(router.urls))
]