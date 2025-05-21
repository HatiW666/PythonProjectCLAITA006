# Inserimento di un record nella tabella
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)

cursor = conn.cursor()

sql = "INSERT INTO studenti (nome, voto) VALUES (%s, %s)"
nome = input("Inserisci nome: ")
voto = float(input("Inserisci voto: "))
valori = (nome, voto)

cursor.execute(sql, valori)
conn.commit()

print(f"{cursor.rowcount} record inserito.")

cursor.close()
conn.close()