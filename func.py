from data import*

 #if action == '2':

def infoplayer():
   print(f'игрок-{player["name"]} ')
print(f'здоровье-{player["hp"]}')
print(f'скорость-{player["speed"]}')
print(f'сила-{player["strong"]}')

def training(training_type):
   pass
def fight(current_enemy0):
    enemy = enemies[current_enemy0]

    while player['hp']>0 and enemy['hp']>0:
        
        player['hp'] -= enemy['attack']
        enemy['hp'] -= player['attack']
        
        print(f'Здоровье игрока = {player["hp"]}, Враг нанёс {enemy["attack"]} урона')
        print(f'Здоровье врага = {enemy["hp"]}')

