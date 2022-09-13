# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

sec = int(input('input time in seccond: '))
hour = sec//3600
rest_minutes = sec%3600
min_1 = rest_minutes//60
rest_sec = rest_minutes%60
print(f'{sec} this {hour} hours, {min_1} minutes and {rest_sec} seconds')
