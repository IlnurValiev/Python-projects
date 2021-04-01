import random
print('Я подброшу монетку 1000 раз. Угадай, сколько раз выпадет Орел?(нажми Enter для продожения)')
input()
flips = 0
heads = 0
while flips < 10000:
    if random.randint(0,1)==1:
        heads = heads + 1

    flips = flips + 1


    if flips == 9000:
            print('9000 подкидываний и "Орел" выпал ' + str(heads) + ' раз.')
    if flips == 1000:
            print('При 1000 бросках, "Орел" выпал ' + str(heads) + ' раз.')
    if flips == 5000:
            print('Полпути пройдено и "Орел" выпал ' + str(heads) + ' раз.')

print()
print('Из 1000 подбрасываний монетки "Орел" выпал ' + str(heads) + ' раз!')
print('Насколько вы близки к правильному ответу?')
