from django.contrib import admin
from .models import Author, FileBook, AudioBook

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status')
    list_filter = ('status',)
    list_editable = ('status',)

@admin.register(FileBook)
class BookAdmin(admin.ModelAdmin):
    list_display = ('document_filename', 'id', 'status', 'file_link',)
    list_filter = ('status', 'created_at')
    list_editable = ('status', 'file_link')

@admin.register(AudioBook)
class BookAdmin(admin.ModelAdmin):
    list_display = ('document_filename', 'id', 'status', 'audio_link',)
    list_filter = ('status', 'created_at')
    list_editable = ('status', 'audio_link')