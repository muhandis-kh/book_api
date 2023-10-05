import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')

ADD_FILES_LINK = os.getenv('ADD_FILES_LINK')
ADD_AUDIOS_LINK = os.getenv('ADD_AUDIOS_LINK')

DOCUMENT_FILES = os.getenv('DOCUMENT_FILES')
AUDIO_FILES = os.getenv('AUDIO_FILES')

korrektor_token = os.getenv('korrektor_token')

django_secret_key = os.getenv('DJANGO_SECRET_KEY')

admin_token = os.getenv('ADMIN_TOKEN')