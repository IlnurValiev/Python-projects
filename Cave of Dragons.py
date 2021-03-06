import random
import time

def display_intro():
    print('''Вы находитесь на планете Дракарис, населенной драконами. 
Перед собой вы видите две пещеры.
В одной из них - дружелюбный дракон по имени Дрогон,
который готов поделиться с вами сокровищами,
оставленными древними поселенцами планеты.
В другой - жадный и злой мертвый дракон Балерион Ужасный,
желающий поразить вас своим мертвым дыханием и обратить в нежить.''')
    print()


def choose_cave():
    cave = ''
    while cave !='1' and cave !='2':
        print('В какую пещеру вы хотите войти? (нажмите клавишу 1 или 2)')
        cave = input()
    return cave

def check_cave(choosen_cave):
    print('''Вы приближаетесь к пещере...
Открываете дверь и видите перед собой ступеньки вниз.
Неспешно начинаете спускаться по ним в глубь таинственного подземелья...''')
    print()
    time.sleep(10)
    print('''Ее тревожащая темнота заставляет вас трепещать от страха.
Вы ощущаете едкий запах серы,
и запах этот усиливается по мере продвижения в недры пещеры.
Пламя факела, что освещает путь, начинает небрежно трепыхаться...''')
    print()
    time.sleep(12)
    print('''Ступеньки закончились, и перед вашим взором раскрылось пространство, 
в котором не видно ни потолка, ни стен напротив.
Вы слышите неторопливое дыхание древнего огнедыщащего чудовища,
и ваше тело начинает покрываться гусиной кожей...''')
    print()
    time.sleep(12)
    print('''Внезапно пещера содрогается, раздается пронзительный вопль, 
и в след за звуком размаха крыльев, факел в ваших руках затухает.
Дракон, извергнув пламя, в миг зажигает несколько десятков люстр,
и вы видите перед собой причину вашего прибытия в Дракарис...''')
    print()
    time.sleep(15)

    friendlyCave = random.randint(1,2)

    if int(choosen_cave) == friendlyCave:
        print('''Дракон извергает огонь в сторону стены, в ней открываются огромные ворота,
за которыми стоит сундук с гербом в виде красного трехголового дракона на черном фоне,
а под гербом надпись \"Пламя и кровь\".
Дрогон отворачивается от вас, сворачивается и засыпает.
На этот раз вам повезло.''')
    else:
        print('''При виде ужасающе огромного чудовища вас бросает в дрожь: 
драконов таких размеров вы еще не встерчали, хотя повидали их достаточно много.
Но больше всего пугало вас другое - пламя, которое он извергнул,
чтобы осветить пещеру, было синим и отдавало жутким, пробивающим до костей морозом.
Последним, что вы видели в своей жалкой жизни,
была громадная пасть Балериона Ужасного с извергающимся из нее синим пламенем.
Вы встали на службу нежити.
Увидимся по другую сторону жизни.''')

playAgain = "Да"

while playAgain == "Да" or playAgain == "Д" or playAgain == "д" or playAgain == "да":
    display_intro()
    caveNumber = choose_cave()
    check_cave(caveNumber)
    
    print()

    print("Попытаете удачу еще раз?")
    playAgain = input()
