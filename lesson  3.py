x = int(input('x = '))

if x > 10:
    print('Всем привет')

print()

d = None

if d is not None:
    pass

x = int(input('x = '))


if x < 0:
    x += 1

print(x)

print()

x = int(input('x = '))

if 0 < x < 7:
    print('Все хорошо')
    y = 5 * x
    if y < 0:
        print('Все плохо')
    else:
        if y > 0:
            print('Все отлично')
        else:
            print('y = 0')

print('''Меню:
      1. Работа
      2. Учеба
      3. Карьерный рост
''')

choice = int(input('Ваш выбор: '))

if choice == 1:
    print('Вы молодец')
elif choice == 2:
    print('Вы молодец2')
elif choice == 3:
    print('Вы молодец3')
else:
    print('Вы не молодец')

g = True


if g:
    state_msg = 'Готов'
else:
    state_msg = 'Не готов'

print(g)

print()

string = input('Напишите что-либо: ')
if string:
    print('Ваша строка {}'.format(string))

number = int(input('Напишите число: '))
if number:
    print('Число не равно нулю')
else:
    print('Вы не написали число')