# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

# def check_database(db):
#     print(db.get('iseedeadpeople'))
#     print(db.keys())
#     print(db.values())

def check_user(username, password):
    if username in user_database.keys() and password == user_database.get(username) :
        return True
    else:
        return False
# check_database(user_database)
print(check_user('user', 'password'))