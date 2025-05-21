def require_admin(func):
    def wrapper(user):
        if user['is_admin'] is True:
            print('OK')
        else:
            print('Access denied')

    return wrapper


def logger(func):
    def wrapper():
        print(f'\nВызов функции {func.__name__}')
        func()
        print(f'Функция {func.__name__} завершена')

    return wrapper


@require_admin
def delete_user(user):
    print(f"User {user['name']} deleted")



delete_user({"name": "John", "is_admin": True})  # OK
delete_user({"name": "Alice", "is_admin": False})  # Access denied


@logger
def say_hello():
    print("Hello!")

say_hello()
