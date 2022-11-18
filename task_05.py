salary = 80
expenses = 90
need = expenses - salary
percent = 0.03
credit = need
for month in range(12):
    credit += need + (need * round(percent, 2))
    percent += 0.03
print(f'Необходимо взять в долг {credit} рублей')

# Хорошо. 
# Вариант через while
# Решение 2
salary, expenses = 10000, 12000

i = expenses - salary
m = 0
debt = 0
while m < 12:
    mx = i * (1.03 ** m)
    debt += mx
    m += 1
print(f'Необходимо взять в долг {round(debt, 2)} рублей')
