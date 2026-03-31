import psycopg2

connection_parametrs={
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "Niyaz015016"
}
try:
    conn = psycopg2.connect(**connection_parametrs)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS phonebook(id SERIAL PRIMARY KEY, name TEXT, address VARCHAR(255), number VARCHAR(255))")
    conn.commit()
    print("Table created")
except Exception as error:
    print("Error!!!")
finally:
    cur.close()
    conn.close()
    print("Closed")