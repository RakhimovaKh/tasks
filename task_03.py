month = input('Введите номер месяца: ')
day_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if month.isdigit():
    month = int(month)
    print(day_per_month[month])
else:
    print('Вы ввели некорректные данные')
