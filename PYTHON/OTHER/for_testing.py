##
# Напишите программу, которая выводит на экран фразу в формате:
# Hello, <name>! Today is <dayofweek>. Have a nice day
# пример: Hello, John! Today is Friday. Have a nice day!
# информация о пользователе содержится в следующих переменных:
# user_name - имя пользователя, dayofweek - название дня недели
# ! обязательное условие - задача должна быть решена с использованием метода format
# ! Codeboard не поддерживает f-строки, поэтому используйте метод format()

name = 'John'
dayofweek = 'Friday'

print('Hello, {}! Today is {}. Have a nice day!'.format(name, dayofweek))
#ваш код здесь

def get_currency_by_date(cur_date, currency):
    return None
cur_date = input('Enter date: ')
currency = input('Enter currency: ')
rate = get_currency_by_date(cur_date, currency)
print('The', currency, 'currency rate on the date', cur_date,'is', rate)