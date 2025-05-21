# Creazione di una tabella nel database
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS studenti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    voto FLOAT
)
""")

print("Tabella creata o già esistente.")

cursor.close()
conn.close()
