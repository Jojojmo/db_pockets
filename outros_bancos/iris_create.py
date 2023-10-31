import sqlite3
import csv

conn = sqlite3.connect('outros_bancos\\iris.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE iris (
        sepal_length REAL,
        sepal_width REAL,
        petal_length REAL,
        petal_width REAL,
        species TEXT
    )
''')

with open('outros_bancos\\iris.csv', 'r', newline='') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    next(leitor)  # Ignora a primeira linha (cabeçalho)
    for linha in leitor:
        cursor.execute('INSERT INTO iris VALUES (?, ?, ?, ?, ?)', linha)

conn.commit()
conn.close()
