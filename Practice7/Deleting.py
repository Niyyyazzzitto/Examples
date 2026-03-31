import psycopg2

connection = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "Niyaz015016"
}
a = input()
try:
    conn = psycopg2.connect(**connection)
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM phonebook
    WHERE name = %s
""", (a,))
    conn.commit()
    print("Info is deleted")
except Exception as error:
    print(error)
finally:
    cur.close()
    conn.close()