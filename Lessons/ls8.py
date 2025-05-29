import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

connect.commit()

def add_user(name: str, age: int, hobby="None"):

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} - Добавили")

# add_user("user1", 33, "Спать")
# add_user("user2", 33, "Спать")
# add_user("user3", 33, "Спать")
# add_user("user4", 33, "Спать")


def get_all_users():

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    for user in users:
        print(f"{user[0]}, {user[1]}, {user[2]}")

# get_all_users()


def update_user(name, id):

    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name,  id)
    )

    print("Обновлен пользователь")

    connect.commit()

update_user("user3", 4)


def delete_user(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    connect.commit()
    print('Пользователь удален!!')

# delete_user(3)
