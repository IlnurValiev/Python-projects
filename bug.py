import random

def play_again():
    print('Хотите сыграть еще? (да, нет)')
    return input().lower().startswith('д')

def get_guess():
    while(True):
        answer = input().split()
        if len(answer) > 1:
            print('Введите одно число')
        elif str(answer[0]) in 'йцукенгшщзхъфывапролджэ\.юбьтимсчяqwertyuiop[]]\';lkjhhgfdsazxcvbnm,./+_)(*&^%$#@!!"№;%:?*()_`~ё':
            print('Введите число')
        else: return answer[0]

while(True):
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)

    print('Сколько будет: ' + str(number1) + ' + ' + str(number2) + '?')
    
    while(True):
        answer = get_guess()
        if int(answer) == number1 + number2:
                print('Верно!')
        else:
            print('Нет! Правильный ответ - ' + str(number1 + number2))
            break
    if not play_again():
        break
