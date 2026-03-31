import psycopg2
import csv

connection = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "Niyaz015016"
}
a = input()
b = input()
c = input()
try:
    conn = psycopg2.connect(**connection)
    cur = conn.cursor()
    cur.execute("""
    UPDATE phonebook
    SET name = %s, number = %s
    WHERE name = %s
""", (a, b, c))
    conn.commit()
    print("Yes")
except Exception as error:
    print(error)
finally:
    cur.close()
    conn.close()