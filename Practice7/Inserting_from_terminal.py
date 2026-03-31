import psycopg2

connection = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "Niyaz015016"
}
a, b = input().split()
try:
    conn = psycopg2.connect(**connection)
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, number) VALUES (%s, %s);", (a, b))
    conn.commit()
    print("Info is added")
except Exception as error:
    print(error)
finally:
    cur.close()
    conn.close()