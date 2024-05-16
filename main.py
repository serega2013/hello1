from data import*
from func import*
name = input('Введите своё имя, путник: ')
player['name'] = name

#print('Ваше имя =', player['name'])
current_enemy=0
while True:
 action = input('''Выбери действие:
1 - бой!  //в разработке
2 - Информация об игроке  
3 - Информация о  противнике  //в разработке
4 - покажи инвентарь  //в разработке
5 - Тренеруйся  //в разработке
6 - Магаз  //в разработке
7 -работай негер  //в разработке
''')
 if action =='1':
     fight(current_enemy)

 if action == '2':
    infoplayer()
  
 if action == '5':
     training_type = input('1 - тренировать атаку, 2 - тренировать оборону')
     training(training_type)
   

