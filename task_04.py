from random import choices
from numpy import sum

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
list_of_songs = [time for x in my_favorite_songs for time in x]
list_of_songs = list_of_songs[1::2]
time_of_three_songs = choices(list_of_songs, k=3)
print(round(sum(time_of_three_songs), 2))
