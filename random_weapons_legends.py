from random import randint
from os import system
from time import sleep

def show_legend(weapon, legends, armas, x, esc):
    if x == 1:
        legend = randint(0, len(legends[weapon])-1)
        
        print('\nA ARMA selecionada foi:', ''.join(armas[esc]))
        print('A LENDA selecionada foi:', legends[weapon][legend])
        

    elif x == 2:
        legend = randint(0, len(legends[weapon])-1)

        print('\nA ARMA selecionada foi:', ''.join(armas[weapon]))
        print('A LENDA selecionada foi:', legends[weapon][legend])

    a = input('\nAperte enter para continuar...')
    system('cls')

armas = ['Axe'], ['Hammer'], ['Katars'], ['Rocket Lance'], ['Spear'], ['Blasters'], ['Orb'],['Bow'], ['Greatsword'], ['Scythe'], ['Gauntlets'], ['Sword'], ['Cannon']

legends = [
    
    #Axe
    ['Teros', 'Brynn', 'Barraza', 'Azoth', 'Ulgrim', 'Jhala', 'Ragnir', 'Xull', 'Rayman', 'Volkov'],
    #Hammer
    ['Bödvar', 'Cassidy', 'Gnash', 'Scarlet', 'Sentinel', 'Teros', 'Kor', 'Yumiko', 'Thor', 'Magyar'],
    #Katars
    ['Quenn Nai', 'Sentinel', 'Lucien', 'Asuri', 'Ember', 'Ragnir', 'Caspian', 'Lin Fei', 'Mako'],
    #Rocket Lance
    ['Orion', 'Lord Vraxx', 'Sr. Roland', 'Scarlet', 'Ulgrim', 'Artemis', 'Vector'],
    #Spear
    ['Orion', 'Gnash', 'Queen Nai', 'Hattori', 'Ada', 'Brynn', 'Wu Sang', 'Mirage', 'Kaya', 'Dusk', 'Arcadia'],
    #Blasters
    ['Cassidy', 'Lord Vraxx', 'Thatch', 'Ada', 'Lucien', 'Barraza', 'Diana', 'Cross', 'Nix', 'Isaiah', 'Reno'],
    #Orb
    ['Dusk', 'Fait', 'Thor', 'Petra', 'Reno', 'Ezio'],
    #Bow
    ['Ember', 'Azoth', 'Koji', 'Diana', 'Yumiko', 'Kaya', 'Zariel', 'Vector', 'Minun'],
    #Greatsord
    ['Jaeyun', 'Mako', 'Magyar', 'Arcadia'],
    #Scythe
    ['Mirage', 'Nix', 'Mordex', 'Artemis', 'Jiro', 'Fait', 'Volkov', 'Munin'],
    #Gauntlets
    ['Kor', 'Wu Sang', 'Val', 'Cross', 'Mordex', 'Caspian', 'Zariel', 'Rayman', 'Petra', 'Onyx'],
    #Sword
    ['Bödvar', 'Hattori', 'Sr. Roland', 'Thatch', 'Asuri', 'Koji', 'Jhala', 'Val', 'Sidra', 'Jiro', 'Jaeyun', 'Ezio'],
    #Cannon
    ['Sidra', 'Xull', 'Isaiah', 'Lin Fei', 'Onyx']
            ]

while True:
    system('cls')
    while True:
        
        print('''\nEscolha uma das opçoes abaixo:
    [1] Escolher arma
    [2] Arma e Lenda aleatórias''')

        try:
            esc_main = int(input('\n> '))
        except:
            print('Opção indisponível!')
            sleep(2.5)
            break

        if esc_main == 1:
            print('''
                ====ESCOLHA DE ARMA====

[1] Axe		[2] Hammer      [3]  Katars     [4]  Rocket
[5] Spear	[6] Blasters	[7]  Orb	[8]  Bow
[9] Greatsword	[10] Scythe	[11] Gauntlets	[12] Sword
                                                [13] Cannon''')

            try:
                esc= int(input('\n> ')) -1
            except:
                print('Opção indisponível!')
                sleep(2.5)
                break
                
            weapon = esc
            show_legend(weapon, legends, armas, 1, esc)

        elif esc_main == 2:

            esc = ''
            weapon = randint(0, len(armas)-1)
            show_legend(weapon, legends, armas, 2, esc)

        else:
            print('Opção indisponível!')
            sleep(2.5)
            break
