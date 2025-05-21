# Connessione a un database MySQL
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)

print("Ciao, mondo!")

print("Connessione avvenuta con successo!")

conn.close()
