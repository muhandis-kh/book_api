import psycopg2



# """"""""""""""""""""""""""""""""""""""""""""""""

import csv
lent = 0
with open(r"C:\Users\User\Desktop\telegram-channel scrap data\telegram-tracker\output\data\msgs_dataset.csv", newline='', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    reader = csv.DictReader(csvfile)
    connection = psycopg2.connect(user="postgres",
                              password="obidcan124578",
                              host="localhost",
                              port="5432",
                              database="book_api")
    cursor = connection.cursor()

    for row in reader:
        # if row['document_type'] == 'application/pdf':
        #     pass
            # lent.append(row['document_type'])
        # if row['document_type'] == 'image/vnd.djvu':
        #     print(row)
        # if row['document_type'] == 'video/x-msvideo':
        #     print(row['msg_link'])
        
        if row['document_type'].startswith('application/'):
        #     if row['document_type'] == 'application/pdf':
        #         pass
        #     elif row['document_type'] == 'application/x-fictionbook+xml' or row['document_type'] == 'application/zip' or row['document_type'] == 'application/x-rar' or row['document_type'] == 'application/x-ms-dos-executable' or row['document_type'] == 'application/x-rar-compressed' or row['document_type'] == 'application/vnd.openxmlformats-officedocument.presentationml.presentation' or row['document_type'] == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' :
        #         pass
        #     else:
        #         print(row['document_type'])
        #         print(row['msg_link'])
        #     # else:
        #     #     print(row['document_type'])
        #         # print(row['msg_link'])
            if row['document_type'] == "application/x-ms-dos-executable":
                pass
            else:
                print(row)
                break;
                # try:


                #     postgres_insert_query = """ INSERT INTO book_api_filebook (name, type, category, photo, file_link, audio_link, download_count, status, created_at, author_id) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s)"""
                #     record_to_insert = ('Diyori Bakr', 'PDF', 'Badiiy', 'null', 'https://t.me/TKTI_library/8655', 'null', 0, 'true', '2023-06-02 17:27:48.856825+05', '1')
                #     cursor.execute(postgres_insert_query, record_to_insert)

                #     connection.commit()
                #     count = cursor.rowcount
                #     print(count, "Record inserted successfully into mobile table")

                # except (Exception, psycopg2.Error) as error:
                #     print("Failed to insert record into mobile table", error)

                # finally:
                #     # closing database connection.
                #     cursor.close()
                #     connection.close()
                #     print("PostgreSQL connection is closed")  


