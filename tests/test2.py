import psycopg2
import re 
import time
from autoslug import AutoSlugField
import django
django.setup()
from pprint import pprint
from django.core.management import call_command
from book_api.models import FileBook
import datetime

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))
    # return len(text.encode("ascii", "ignore")) < len (text)

def Find(string):
    x=string.split()
    res=[]
    for i in x:
        if i.startswith("https:") or i.startswith("http:") or i.startswith("@") or i.startswith("[@"):
            res.append(i)
    return res


from korrektor_py import Korrektor

TOKEN = "v3l4a5e3b485r3f5x35565y534v2f4r595s4e3w3h5v3x475t3u273o315p3u2y2"
korrektor = Korrektor(TOKEN)
import csv

alphabet = "latin"


# """"""""""""""""""""""""""""""""""""""""""""""""

lent = 1
with open(r"C:\Users\User\Desktop\telegram-channel scrap data\telegram-tracker\output-vkb_baza_audio\data\msgs_dataset.csv", newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    reader = csv.DictReader(csvfile)
    # connection = psycopg2.connect(user="postgres",
    #                           password="obidcan124578",
    #                           host="localhost",
    #                           port="5432",
    #                           database="book_api")

    totalrows = 681661
    basliklar = ['id', 'document_filename', 'description', 'type', 'file_link', 'channel_name']
    with open('data_audios.csv', 'w', encoding="utf8", newline='') as dosya:
        yazici = csv.writer(dosya)
        yazici.writerow(basliklar)
        
        for row in reader:

                    document_filename = row['document_filename']
                    if Find(document_filename):
                        
                        for msg in Find(document_filename):
            
                            document_filename = row['document_filename'].replace(msg, '')
                            
                    message = row['message']
                    
                    if Find(row['message']):
                        for msg in Find(row['message']):  
                            if msg.startswith('@'):
                                manba = msg
                                pass
                            else:  
                                    message = message.replace(msg, '')     
                        try:
                            message = message.replace("👉", '')
                            message = message.replace("Kanalimiz:", '')
                            message = message.replace("Manzilimiz:", '')
                            message = message.replace("Obuna bo'ling:", '')
                            message = message.replace("Ulashing:", '')
                            message = message.replace("kanali", '')
                            message = message.replace("Rasmiy kanalimiz!", '')
                            message = message.replace("Kutubxona guruhimiz!", '')
                            message = message.replace("()", '')
                            message = message.replace("Kanalga a'zo bo'lish", '')
                            message = message.replace("Do'stlaringizga ham ulashing", '')
                            message = message.replace("va do'stlaringizni kanalga taklif eting.", '')
                            message = message.replace("- IT va boshqa istalgan sohada bepul darslar makoni", '')
                            message = message.replace("BIZGA QO'SHILING", '')
                            message = message.replace("Guruh", '')
                            message = message.replace("Kanal", '')
                            message = message.replace("Kino topib beruvchi ajoyib bot", '')
                            message = message.replace("telegram kanali", '')
                            message = message.replace("bilan kitoblarni tez va oson toping!", '')
                        except:
                            pass
                    
                    caption = message
                    try:
                        if has_cyrillic(document_filename):
                            result = korrektor.transliterate(alphabet, document_filename)
                            document_filename = result.text
                    except Exception as e:
                        print(e)
                        pass
                    
                    document_filename = document_filename.replace('_', ' ')
                    document_filename = document_filename[:-4]

                    foiz = (lent * 100) / totalrows
                    second = totalrows / 30
                    time = str(datetime.timedelta(seconds=second))
                    
                    # cursor = connection.cursor()
                    try:
                        secilen_sutunler = [row['signature'], row['document_filename'], row['message'], 'audio', row['msg_link'], manba]
                        yazici.writerow(secilen_sutunler)
                        # file = FileBook.objects.create(document_filename=document_filename, description=caption, author=1, type=row['type'], category=None, photo=None, file_link=row['file_link'], channel_name=row['channel_name'], download_count=0 )
                        
                        # postgres_insert_query = """ INSERT INTO book_api_filebook (document_filename, slug, description, type, category, photo, channel_name, file_link, download_count, status, created_at, author) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                        # record_to_insert = (document_filename, AutoSlugField(populate_from=document_filename, unique=True), row['message'][:300], row['document_type'], 'null', 'null', row['channel_name'], row['msg_link'], 0, 'true', '2023-06-14 12:09:48.856825+05', row['document_filename'][:20] )
                        # cursor.execute(postgres_insert_query, record_to_insert)

                        # connection.commit()
                        # count = cursor.rowcount
                        print(f"Record inserted successfully into mobile table {lent} / 681661   {str(foiz)[:5]}% {time} qoldi")
                        totalrows -= 1
                        lent += 1
                        print("************************************************************************************************")
                        # time.sleep(0.03)
                    except Exception as error:
                        
                        print("Failed to insert record into mobile table", error)
                        pass




