from data import *




def info_player():
    print(f'Игрок = {player["name"]}')
    print(f'здоровье - {player["hp"]}')
    print(f'урон - {player["attack"]}')
    print(f'деньги - {player["money"]}')
    

def fight(current_enemy0):
    enemy = enemies[current_enemy0]

    while player['hp']>0 and enemy['hp']>0:

        player['hp'] -= enemy['attack']
    enemy['hp'] -= player['attack']
 
    print(f'Здоровье игрока ={player["hp"]}, Враг нанес {enemy["attack"]}')
    print(f'Здоровье врага = {enemy["hp"]}')

    print()



    if enemy['hp'] <=0:
        print(f'Противник - {enemy["name"]}; {enemy["win"]}')






