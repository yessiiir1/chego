m = [5, 4, 2, 23]
M = ['a', 'b', 'c', 'd']
Array = []

print('Список чисел:', m)
print('Список символов:', M)
print('Пустой список:', Array)

m = [1,2,3,4,5,6,7,12325]
print(m[0])
print(m[1])
index = int(input('Введите номер элемента: '))
el = m[index]
print(el)

m = [1,2,3,4,5,6,7]
p = m[-2]
print(p)
r = m[0] + m[-1]
print(r)


mm = [1,2,3,4,5,6,7]

m = mm[0:3]
print(m)
print(mm[2:-2])
print(mm[4:5])

m = [1,2,3,4,5,6,7]
print(m[2:])
print(m[:-2])
print(m[::-1])

m = [1,2,3,4,5,6,7]


value = int(input('Введите число: '))


if value in m:
    print('Число входит в список')
else:
    print('Число не входит в список')

my_list = [1, 5, 1, 3, 7]
print(len(my_list))

string = "Hi!!!!"

print(string[0])
print(string[2])
print(string[-1])

string = "a string"
print(string[3:-1])
print(string[3] + string[-2:])

string = input('Введите строку: ')
if 'ф' in string:
    print('В этой строке есть символ "ф".')
else:
    print('В этой строке нет символа "ф".')

string = input('Введите строку: ')
print('Длина этой строки:', len(string))

m = []
m.append(117126312)
print(m)

m = [1,2,3,4,5,6,7,8]
del m[4]

m = [1,2,3,4,5,6,7,8]
print(m)
l = len(m)
i = l
while not -l <= i < l:
    i = int(input('Введите индекс элемента списка (от %d до %d): '
                      % (-l, l - 1)))
value = int(input('Введите новое значение заданного элемента: '))
m[i] = value
print(m)

m = [1,2,3,4,5,6,7,8]
for a in m:
    print('{} ^ 2 = {}'.format(a, a ** 2))

empty = list()
print(empty)

num = list(range(1000))
print(num)

chars = list("a string")
print(chars)

n = 10

fibs = [1, 1]
for i in range(n - 2):
    fibs.append(fibs[i] + fibs[i + 1])

print(fibs)





