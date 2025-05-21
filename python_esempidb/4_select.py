# Selezione e stampa di tutti i record
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)

cursor = conn.cursor(dictionary = True)

cursor.execute("SELECT * FROM book")
risultati = cursor.fetchall()

for libro in risultati:
    if libro["year"] > 2010:
        print(libro["title"])

# for (id, nome, voto) in risultati:
#     print(f"{id} - {nome} - {voto}")

cursor.close()
conn.close()
