import random as ran

GIBBET_PICS_EASY = ['''
      ________
            |
            |
            |
            |
            |
            |
      =============''', '''
      ________
       |    |
            |
            |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
            |
            |
            |
            |
      =============''', ''' 
      ________
       |    |
       O    |
       |    |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|    |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
       |    |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
       |    |
      /     |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
       |    |
      / \   |
            |
      =============''', '''

       _______
       |    |
       O]   |
      /|\   |
       |    |
      / \   |
            |
      =============''', '''
      _______
       |    |
      [O]   |
      /|\   |
       |    |
      / \   |
            |
      =============''']

GIBBET_PICS_MIDDLE = ['''
      ________
            |
            |
            |
            |
            |
            |
      =============''', '''
      ________
       |    |
            |
            |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
            |
            |
            |
            |
      =============''', ''' 
      ________
       |    |
       O    |
       |    |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|    |
            |
            |
            |
      =============''','''
      ________
       |    |
       O    |
      /|\   |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
       |    |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
       |    |
      /     |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
       |    |
      / \   |
            |
      =============''']

GIBBET_PICS_HARD = ['''
      ________
       |    |
            |
            |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
            |
            |
            |
            |
      =============''', ''' 
      ________
       |    |
       O    |
       |    |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|    |
            |
            |
            |
      =============''','''
      ________
       |    |
       O    |
      /|\   |
            |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
       |    |
            |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
       |    |
      /     |
            |
      =============''', '''
      ________
       |    |
       O    |
      /|\   |
       |    |
      / \   |
            |
      =============''']

wordList = {
"Животные" : '''аист акула бабуин баран 
барсук бобр бык верблюд волк воробей ворон 
выдра голубь гусь жаба зебра змея 
индюк кит кобра коза козел койот корова кошка 
кролик крыса курица лама ласка лебедь лев 
лиса лосось лось лягушка медведь моллюск моль мул 
муравей мышь норка носорог обезьяна
овца окунь олень орел осел панда паук питон 
попугай пума семга скунс собака сова тигр тритон 
тюлень утка форель хорек черепаха ястреб ящерица'''.split(),
"Фрукты" : ''' яблоко апельсин лимон лайм груша 
мандарин виноград грейпфрут персик банан абрикос
манго банан нектарин '''.split(),
'Фигуры':'''квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм
пятиугольник шестиугольник восьмиугольник'''.split(),
'Мужские имена': '''Александр
Алексей
Альберт
Анатолий
Андрей
Аркадий
Антон
Артемий
Артём
Артур
Богдан
Борис
Вадим
Валентин
Валерий
Василий
Виктор
Виссарион
Виталий
Владимир
Вячеслав
Всеволод
Владлен
Геннадий
Георгий
Герасим
Герман
Глеб
Григорий
Денис
Дмитрий
Евгений
Евсей
Егор
Емельян
Ефим
Иван
Игнатий
Игорь
Илья
Иннокентий
Ираклий
Кирилл
Константин
Лев 
Леонид
Леонтий
Максим
Марк
Матвей
Мирослав
Марат
Михаил
Никита
Николай
Олег
Павел
Петр
Потап
Прохор
Родин
Роман
Руслан
Ростислав
Савелий
Семен
Сергей
Станислав
Степан
Тарас
Тимофей
Тимур
Тихон
Федор
Филипп
Эдуард
Ильнур
Ильшат
Камиль
'''.split(),
'Женские имена': '''
Александра
Алина
Алла
Анастасия
Ангелина
Анжела
Анжелика 
Анна 
Антонина
Анфиса
Валентина
Валерия
Варвара
Василиса
Вера 
Вероника
Виктория 
Галина
Дарья
Евгения
Екатерина
Елена
Елизавета
Жанна

Зинаида
Злата
Зоя
Ирина
Карина
Каролина 
Кира
Клавдия
Ксения
Лада 
Лариса 
Лидия 
Лилия 
Любовь 
Людмила

Маргарита
Марина
Мария
Мирослава

Надежда 
Наталья
Нина
Нонна Ольга Оксана 
Пелагея Полина 
Рада 
Раиса
Римма
Светлана
Серафима
Снежана
София

Таисия
Тамара 
Татьяна
Ульяна
Урсула
Фаина
Юлия
Яна
Ярослава
Нигина
Гузаль
'''.split()
}


def getRanWord(wordDict):
    wordKey = ran.choice(list(wordDict.keys()))
    wordIndex = ran.randint(0, len(wordKey) - 1)
    return wordDict[wordKey][wordIndex], wordKey

def displayBoard(missedLetters, correctLetters, secretWord):
    print(GIBBET_PICS[len(missedLetters)])
    print()

    blanks = '_'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i].lower() in correctLetters:
            blanks = blanks[:i]+secretWord[i]+blanks[i+1:]
    
    print("Загаданное слово:", end=' ')
    for letter in blanks:
        print(letter, end=" ")
    print()
    
    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=', ')
    print()
    print()

def getGuess(alreadyGuessed):
    while True:
      print("Введите букву")
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
          print("Введите одну букву")   
      elif guess in alreadyGuessed:
          print("Вы уже называли эту букву. Назовите другую")
      elif guess not in "йцукенгшщзхъфывапролджэюбьтимсчя":
          print("Нужно ввести букву русского алфавита")
      else:
          return guess

def playAgain():
    print("Хотите сыграть еще?")
    return input().lower().startswith('д')

def selectDifficulty():
    print("Выберите сложность: т - трудно(" + str(len(GIBBET_PICS_HARD)) + " попыток), с - средне(" + str(len(GIBBET_PICS_MIDDLE)) + " попыток), л - легко(" + str(len(GIBBET_PICS_EASY)) + " попыток)")
    while True:
      dif = input()
      dif = dif.lower()
      if len(dif) != 1:
          print("Введите одну букву")
      elif dif == 'т':
          return GIBBET_PICS_HARD
      elif dif == 'с':
          return GIBBET_PICS_MIDDLE
      elif dif == 'л':
          return GIBBET_PICS_EASY
      else:
          print("Введите одну из трех букв: т, с, л")     

print("В И С Е Л И Ц А")

secretWord, secretSet = getRanWord(wordList)
missedLetters = ''
correctLetters = ''
gameIsDone = False
beginning = True

while True:
    if beginning: 
        GIBBET_PICS = selectDifficulty()
        beginning = False

    print("Категория: " + secretSet)
    
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters) #вводим букву из клавы
    
    foundAllLetters = True
    
    for i in range(len(secretWord)):
        if(secretWord[i].lower() == guess):
            correctLetters = correctLetters + guess
            
            for k in range(len(secretWord)):
                if secretWord[k].lower() not in correctLetters:
                  foundAllLetters = False
                  break

            if foundAllLetters:
                print('ДА! Я загадал слово - "'+ secretWord +'"! Вы угадали!')
                gameIsDone = True
            break

        elif(guess not in missedLetters and guess not in secretWord):
            missedLetters = missedLetters + guess
        
            if len(missedLetters) == len(GIBBET_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
                gameIsDone = True
        
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            beginning = True
            secretWord, secretSet = getRanWord(wordList)
        else:
            break


