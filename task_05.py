salary = 80
expenses = 90
need = expenses - salary
percent = 0.03
credit = need
for month in range(12):
    credit += need + (need * round(percent, 2))
    percent += 0.03
print(f'Необходимо взять в долг {credit} рублей')
