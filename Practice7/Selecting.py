import psycopg2

connecntion = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "Niyaz015016"
}
a = input()
try:
    conn = psycopg2.connect(**connecntion)
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM phonebook
    WHERE name = %s
""", (a,))
    info = cur.fetchall()
    for i in info:
        print(i)
    conn.commit()
except Exception as error:
    print(error)
finally:
    cur.close()
    conn.close()