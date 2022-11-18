import numpy as np

cities = ['Москва', 'Осака', 'Панама', 'Бразилиа', 'Мадрид']
citizens = [[12_000_000], [3_000_000], [881_000], [3_100_000], [3_300_000]]
print(f'Население {cities[1]} - {citizens[1]} человек')
print(f'Итого размер населения {cities} - ', np.sum(citizens))


# В задаче немного подразумевалось иное. Необходимо было создать список списков с населением
# Такой список запишем в town_population

towns = ['Москва', 'Санкт-Петербург', 'Сочи', 'Владивосток']

town_population = [
    ['Москва', 17000000], 
    ['Санкт-Петербург', 5400000], 
    ['Сочи', 500000], 
    ['Владивосток', 600000]
]



# Решение 1 с функцией
def total_sun(lst):
    total = 0

    for i in lst:
        total += i[1]

    return total

# Решение 2 с функцией в одну строку
def total_sum(lst):
    return sum([i[1] for i in lst])

print(total_sum(population))


# Решение 3 с суммой результатов индексации
population_sum_2 = town_population[0][1] +  town_population[1][1] + town_population[2][1] + town_population[3][1]


# Вывод на консоль ответов
print('Население Москвы -', town_population[0][1], 'человек')

print('Итого размер населения -', population_sum_1, 'человек')

print('Итого размер населения -', population_sum_2, 'человек (решение через for)')

# Решение 4 с filter

print(f'Население {town_population[1][0]}а - {town_population[1][1]} человек')

my_list =sum(town_population, [])

my_filter = list(filter(lambda x: type(x) is int, my_list))

print(f'Итого размер населения - {sum(my_filter)} человек')
