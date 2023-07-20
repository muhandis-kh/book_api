from django.db import models
from autoslug import AutoSlugField
from django.contrib.postgres.search import SearchVectorField, SearchVector

class Author(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Muallif nomi")
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"
        ordering = ["-created_at"]
        
    def __strt__(self):
        return self.full_name

# Create your models here.
class FileBook(models.Model):
    document_filename = models.CharField(max_length=255, verbose_name="Document Nomi")
    slug  = AutoSlugField(populate_from="document_filename", unique=True)
    description = models.TextField(verbose_name="Kitob nomii")
    description_tsvector = SearchVectorField(null=True)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL, related_name='file_book')
    file_link = models.CharField(max_length=255, verbose_name="Kitob file linki", blank=True, null=True)
    channel_name = models.CharField(max_length=255, verbose_name="Kanal nomi")
    download_count = models.PositiveIntegerField(default=0, verbose_name="Yuklab olishlar soni")
    
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.__class__.objects.filter(id=self.id).update(
            description_tsvector=SearchVector(f"to_tsvector('simple', '{self.description}')")
        )
    
    class Meta:
        verbose_name = "File Kitob"
        verbose_name_plural = "File Kitoblar"
        ordering = ['-created_at',]
        
    def __str__(self):
        return self.name
        
class AudioBook(models.Model):
    document_filename = models.CharField(max_length=255, verbose_name="Document Nomi")
    slug  = AutoSlugField(populate_from="document_filename", unique=True)
    description = models.TextField(verbose_name="Kitob nomi")
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL, related_name='audio_book')
    audio_link = models.CharField(max_length=255, verbose_name="Kitob audio linki", blank=True, null=True)
    channel_name = models.CharField(max_length=255, verbose_name="Kanal nomi")
    download_count = models.PositiveIntegerField(default=0, verbose_name="Yuklab olishlar soni")
    
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Audio Kitob"
        verbose_name_plural = "Audio Kitoblar"
        ordering = ['-created_at',]
        
    def __str__(self):
        return self.name
    