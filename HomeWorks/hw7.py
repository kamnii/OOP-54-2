import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')


def add_user(name, age, hobby):

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print('Пользователь добавлен')

# add_user('kaniet', 20, 'sleep')
# add_user('islam', 19, 'sleep')
# add_user('emil', 22, 'sleep')
# add_user('sulaiman', 20, 'sleep')


def get_user_by_id(user_id):

    cursor.execute(
        'SELECT * FROM users WHERE user_id = ?',
        (user_id,)
    )
    user = cursor.fetchall()

    if user:
        for i in user:
            print(f'name: {i[1]}, age: {i[2]}, hobby: {i[3]}')
    else:
        print(None)

# get_user_by_id(20)
