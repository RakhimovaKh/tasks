import numpy as np

cities = ['Москва', 'Осака', 'Панама', 'Бразилиа', 'Мадрид']
citizens = [[12_000_000], [3_000_000], [881_000], [3_100_000], [3_300_000]]
print(f'Население {cities[1]} - {citizens[1]} человек')
print(f'Итого размер населения {cities} - ', np.sum(citizens))
