from connect import connect
import psycopg2
#function 1
def matching_results(part_of_name):
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM matching_results(%s)", (part_of_name,))
        print(cur.fetchall())
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
a = input()
matching_results(a)

#procedure 1
import psycopg2
from connect import connect
def inserting_name_phone(name, address, number):
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute("CALL inserting_name_phone(%s, %s, %s)", (name, address, number))
        conn.commit()
        cur.close()
        print("Yes")
    except Exception as error:
        print(error)
    finally:
        cur.close()
        conn.close()
a = input()
b = input()
c = input()
inserting_name_phone(a, b, c)

#procedure 2
import psycopg2
from connect import connect
def loop_using_proc(p_names, p_numbers):
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute("CALL loop_using_proc(%s, %s)", (p_names, p_numbers))
        conn.commit()
        print("Worked!")
    except Exception as error:
        print(error)
    finally:
        cur.close()
        conn.close()
a = input().split()
b = input().split()
loop_using_proc(a, b)

#function 2
import psycopg2
from connect import connect
def pagination(limits, offset):
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM pagination(%s, %s)", (limits, offset))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        cur.close()
        conn.close()
a = int(input())
b = int(input())
pagination(a, b)

#procedure 3
import psycopg2
from connect import connect
def deleting(usernames):
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute("CALL deleting(%s)", (usernames,))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        cur.close()
        conn.close()
a = input()
deleting(a)