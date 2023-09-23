from radio_list import radio_points
from num import inist
import os
import play_radio_fm
x1 = 1
for x in radio_points:
    print(x1, x)
    x1 += 1
user_radio = input(">> ")
numbers = inist(user_radio)

    
if numbers == True:
    user_radio = int(user_radio)
    listed = []
    for y in radio_points:
        listed.append(y)
    play_radio_fm.play_radio(radio_points[listed[user_radio - 1]], listed[user_radio - 1])
    
else:
    try:
        play_radio_fm.play_radio(radio_points[str(user_radio)], user_radio)
    except:
        print('Такоой радиостанции нет в списке')
