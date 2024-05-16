from data import *
from func import *


print('Вы играете в игру Квест!')
name = input('..Введите свое имя, путник:')
player['name'] = name

current_enemy = 0
print('Приятно познакомиться,', player['name'])


while True:
    action = input('''Выбери действие:
   1 - В бой!  //в разработке
2 - Информация об игроке  
3 - Информация о текущем противнике  //в разработке
4 - Показать инвентарь  //в разработке
5 - Тренировка  //в разработке
6 - Магазин  //в разработке
7 - Получение денег  //в разработке 
 ''')
    
    if action == '2':
        info_player()

    if action == '1':
        fight(current_enemy)
    
    
