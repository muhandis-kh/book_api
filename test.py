import psycopg2
import re 
import time

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))
    # return len(text.encode("ascii", "ignore")) < len (text)

from korrektor_py import Korrektor

TOKEN = "v3l4a5e3b485r3f5x35565y534v2f4r595s4e3w3h5v3x475t3u273o315p3u2y2"
korrektor = Korrektor(TOKEN)
import csv

alphabet = "latin"


# """"""""""""""""""""""""""""""""""""""""""""""""

lent = 1
with open(r"C:\Users\User\Desktop\telegram-channel scrap data\telegram-tracker\output\data\msgs_dataset.csv", newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    reader = csv.DictReader(csvfile)
    connection = psycopg2.connect(user="postgres",
                              password="obidcan124578",
                              host="localhost",
                              port="5432",
                              database="book_api")

    rows = list(reader)
    totalrows = len(rows)
    
    for row in reader:

        if row['document_type'].startswith('application/'):

            if row['document_type'] == "application/x-ms-dos-executable":
                pass
            else:
                document_filename = row['document_filename']
                
                if has_cyrillic(document_filename):
                    result = korrektor.transliterate(alphabet, document_filename)
                    document_filename = result.text
                
                document_filename = document_filename.replace('_', ' ')
                cursor = connection.cursor()
                try:


                    postgres_insert_query = """ INSERT INTO book_api_filebook (document_filename, description, type, category, photo, channel_name, file_link, download_count, status, created_at, author) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    record_to_insert = (document_filename, row['message'][:300], row['document_type'], 'null', 'null', row['channel_name'], row['msg_link'], 0, 'true', '2023-06-14 12:09:48.856825+05', row['document_filename'][:20] )
                    cursor.execute(postgres_insert_query, record_to_insert)

                    connection.commit()
                    count = cursor.rowcount
                    print(f"Record inserted successfully into mobile table {lent} / {totalrows}")
                    lent += 1
                    print("************************************************************************************************")
                    # time.sleep(0.03)
                except (Exception, psycopg2.Error) as error:
                    print(row)
                    print("Failed to insert record into mobile table", error)





