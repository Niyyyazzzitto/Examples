import psycopg2
import csv

connection = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "Niyaz015016"
}
try:
    conn = psycopg2.connect(**connection)
    cur = conn.cursor()
    with open("Practice7/info.csv", mode='r', encoding='utf-8') as file:
        reading = csv.DictReader(file)
        for r in reading:
             name = r['name']
             address = r['address']
             number = r['number']
             cur.execute("INSERT INTO phonebook (name, address, number) VALUES (%s, %s, %s);", (name, address, number))
    conn.commit()
    print("Yes")
except Exception as error:
    print(error)
finally:
    cur.close()
    conn.close()