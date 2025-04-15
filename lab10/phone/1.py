import psycopg2
import csv


def connect():
    return psycopg2.connect(
        dbname="postgres",    
        user="postgres",
        password="19661970",     
        host="localhost",
        port="5432"
    )


def createtable():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("table created")

def selectusers():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook;") 
    results = cur.fetchall() 

    if results:
        print("all users")
        for row in results:
            print(row)  
    else:
        print("empty")

    cur.close()
    conn.close()


def insert_from_input():
    conn = connect()
    cur = conn.cursor()

    name = input("Name: ")
    phone = input("phone number: ")

    cur.execute("""
        INSERT INTO phonebook (name, phone)
        VALUES (%s, %s)
        ON CONFLICT (phone) DO NOTHING;
    """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Data is upploated")

# Добавление из CSV
def insert_from_csv():
    filename = input("Path of CSV file:")
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            name, phone = row
            cur.execute("""
                INSERT INTO phonebook (name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("CSV files data is uploated")


def update_user():
    conn = connect()
    cur = conn.cursor()

    phone = input("number of name what you want change")
    new_name = input("new name")

    cur.execute("""
        UPDATE phonebook
        SET name = %s
        WHERE phone = %s;
    """, (new_name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Data is upploated")


def search_users():
    conn = connect()
    cur = conn.cursor()

    keyword = input("phone or name for searching")
    cur.execute("""
        SELECT * FROM phonebook
        WHERE name ILIKE %s OR phone LIKE %s;
    """, (f'%{keyword}%', f'%{keyword}%'))

    results = cur.fetchall()
    if results:
        print("Found:")
        for row in results:
            print(row)
    else:
        print("**nothing found**")

    cur.close()
    conn.close()


def delete_user():
    conn = connect()
    cur = conn.cursor()

    choice = input("delete by name or number")
    if choice == "1":
        name = input("name: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s;", (name,))
    elif choice == "2":
        phone = input("number: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
    else:
        print("error choice")
        return

    conn.commit()
    cur.close()
    conn.close()
    print("data is deleted")


def menu():
    createtable()
    while True:
        print("\n📞 PhoneBook Menu:")
        print("1. Добавить запись (вручную)")
        print("2. Добавить из CSV")
        print("3. Обновить запись")
        print("4. Найти")
        print("5. Удалить")
        print("6. Вывести")
        print("0. Выход")
        choice = input("chose the option")

        if choice == "1":
            insert_from_input()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_user()
        elif choice == "4":
            search_users()
        elif choice == "5":
            delete_user()
        elif choice == '6':
            selectusers()
        elif choice == "0":
            print("good bay")
            break
        else:
            print("error choice")


if __name__ == "__main__":
    menu()
