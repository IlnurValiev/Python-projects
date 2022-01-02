from sqlite3 import *
import random as rn

symbols = ''
for i in range(32, 127):
    symbols += chr(i)

GET = 'get '
GEN = 'gen '
LIST = 'list'
STOP = 'stop'
INPUT = 'pas_bank:-$ '
DEL = 'del '

table = connect('passwords.db')
cursor = table.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                service_title TEXT NOT NULL UNIQUE ,
                service_password TEXT      
                );''')

command = ''
while(command != STOP):
    if command.startswith(GET):
        service = (command[4:],)
        sql = '''SELECT service_password FROM
                passwords WHERE service_title = ?'''
        cursor.execute(sql, service)
        password = cursor.fetchone()

        try:
            print(''.join(password))
        except TypeError:
            print('No such service')

    if command.startswith(GEN):
        title = command[4:]
        
        n = rn.randint(12,15)
        password = ''.join(rn.sample(symbols, n))

        service = (title, password)
        sql = 'INSERT INTO passwords (service_title, service_password) VALUES (?, ?)'

        try:
            cursor.execute(sql, service)
            print(password)
            table.commit()
        except IntegrityError:
            print('Such service title exits or envalid title')

    if command.startswith(DEL):
        title = (command[4:],)
        sql = 'DELETE from passwords WHERE service_title = ?'
        cursor.execute(sql, title)
        table.commit()

    if command.lower() == LIST:
       cursor.execute('SELECT * from passwords')
       result = cursor.fetchall()
       print()
       print('\n'.join(map(': '.join, result)))

    command = input(INPUT).lower()

table.close()
    
