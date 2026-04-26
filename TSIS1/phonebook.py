import psycopg2
import json
from config import load_config

def connect():
    """Подключение к базе данных PostgreSQL"""
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка подключения: {error}")
        return None

def add_contact(conn):
    name = input("Имя: ")
    email = input("Email: ")
    birthday = input("День рождения (YYYY-MM-DD) или нажми Enter: ") or None
    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO contacts (name, email, birthday) VALUES (%s, %s, %s)", 
                        (name, email, birthday))
            conn.commit()
            print("✅ Контакт успешно добавлен!")
        except Exception as e:
            conn.rollback()
            print(f"❌ Ошибка: {e}")

def add_phone_to_contact(conn):
    name = input("Имя существующего контакта: ")
    phone = input("Номер телефона: ")
    p_type = input("Тип (home / work / mobile): ")
    with conn.cursor() as cur:
        try:
            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, p_type))
            conn.commit()
            print("✅ Телефон добавлен!")
        except Exception as e:
            conn.rollback()
            print(f"❌ Ошибка: {e}")

def move_to_group(conn):
    name = input("Имя контакта: ")
    group = input("Название группы (например, Family, Work): ")
    with conn.cursor() as cur:
        try:
            cur.execute("CALL move_to_group(%s, %s)", (name, group))
            conn.commit()
            print(f"✅ Контакт перенесен в группу '{group}'!")
        except Exception as e:
            conn.rollback()
            print(f"❌ Ошибка: {e}")

def search_contacts_paginated(conn):
    query = input("Введи имя, email или телефон для поиска: ")
    limit = 2  # Количество записей на одной странице
    offset = 0
    with conn.cursor() as cur:
        while True:
            # Вызываем нашу функцию поиска и применяем LIMIT / OFFSET
            cur.execute("SELECT * FROM search_contacts(%s) LIMIT %s OFFSET %s", (query, limit, offset))
            results = cur.fetchall()
            
            print("\n--- Результаты поиска ---")
            if not results:
                print("Ничего не найдено (или конец списка).")
            else:
                for row in results:
                    print(f"Имя: {row[0]}, Email: {row[1]}, Телефон: {row[2]} ({row[3]})")
            
            print("\nНавигация: [n]ext - вперед, [p]rev - назад, [q]uit - выход")
            nav = input("Выбор: ").lower()
            if nav == 'n':
                offset += limit
            elif nav == 'p':
                if offset >= limit:
                    offset -= limit
                else:
                    print("Ты уже на первой странице.")
            elif nav == 'q':
                break

def export_json(conn):
    filename = input("Имя файла для сохранения (например, data.json): ")
    with conn.cursor() as cur:
        cur.execute("""
            SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type 
            FROM contacts c 
            LEFT JOIN groups g ON c.group_id = g.id 
            LEFT JOIN phones p ON c.id = p.contact_id
        """)
        rows = cur.fetchall()
        
        data = []
        for row in rows:
            data.append({
                "name": row[0],
                "email": row[1],
                "birthday": str(row[2]) if row[2] else None,
                "group": row[3],
                "phone": row[4],
                "type": row[5]
            })
            
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ Данные экспортированы в {filename}")

def import_json(conn):
    filename = input("Имя файла для импорта: ")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Файл не найден.")
        return

    with conn.cursor() as cur:
        for item in data:
            cur.execute("SELECT id FROM contacts WHERE name = %s", (item['name'],))
            exists = cur.fetchone()
            
            if exists:
                action = input(f"Контакт '{item['name']}' уже существует. [s]kip (пропустить) или [o]verwrite (перезаписать)? ").lower()
                if action == 's':
                    continue
                elif action == 'o':
                    cur.execute("DELETE FROM contacts WHERE name = %s", (item['name'],))
            
            try:
                # Вставляем контакт
                cur.execute("INSERT INTO contacts (name, email, birthday) VALUES (%s, %s, %s)", 
                            (item['name'], item.get('email'), item.get('birthday')))
                # Если есть группа, вызываем процедуру
                if item.get('group'):
                    cur.execute("CALL move_to_group(%s, %s)", (item['name'], item['group']))
                # Если есть телефон, вызываем процедуру
                if item.get('phone'):
                    cur.execute("CALL add_phone(%s, %s, %s)", (item['name'], item['phone'], item.get('type', 'mobile')))
                
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(f"❌ Ошибка импорта {item['name']}: {e}")
    print("✅ Импорт завершен.")

def main_menu():
    conn = connect()
    if conn is None:
        return

    while True:
        print("\n=== Телефонная Книга (TSIS 1) ===")
        print("1. Добавить новый контакт (базовый)")
        print("2. Добавить телефон существующему контакту")
        print("3. Переместить контакт в группу")
        print("4. Поиск контактов (с пагинацией)")
        print("5. Экспорт в JSON")
        print("6. Импорт из JSON")
        print("0. Выход")
        
        choice = input("Выбери действие: ")

        if choice == '1': add_contact(conn)
        elif choice == '2': add_phone_to_contact(conn)
        elif choice == '3': move_to_group(conn)
        elif choice == '4': search_contacts_paginated(conn)
        elif choice == '5': export_json(conn)
        elif choice == '6': import_json(conn)
        elif choice == '0':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуй снова.")

    conn.close()

if __name__ == '__main__':
    main_menu()