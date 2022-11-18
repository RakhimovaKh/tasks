from random import shuffle
my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02}
items = list(my_favorite_songs.items())
shuffle(items)
sum_of_times = 0
names_of_songs = str()
for key, value in items[0:3]:
    names_of_songs += key
    sum_of_times += float(value)
print('Три песни', names_of_songs, 'звучат:', round(sum_of_times, 2), 'минут')

# Хорошо. Через shuffle тоже хорошо!
