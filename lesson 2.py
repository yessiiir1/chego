x = int(input("Введите значение 1 :"))
y = int(input("Введите значение 2 :"))

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)
print(x ** 0.5)
print(x % y)

print()

print(12 ** 2 - 100 + 20 % 12)

print()


z = 12.123453
print(round(z),round(z,3))

print()

bool1 = True
bool2 = False

print(bool1)
print(bool2)

print()

x = 0.5
y = 3.2


z = 4.2e3
n = 1e-5

print(x,y,z,n)


print(float("0.8"))
print(float(8))

print()

c1 = 5 + 7j
c2 = 1 - 4j

a = 12
b = 5
c3 = complex(a, b)
c4 = complex(7, -9)

print(c1, c2)
print(c3, c4)

print()

x = 'всем привет'
print(x)
print(type(x))

print()


x = 42
print(x)
print(type(x))

print()


a = 5
b = 5
print(a + b)


print()

import math


x = 4.123

print(math.trunc(x), math.floor(x), math.ceil(x))

print(math.pi)
print(math.e)

y = math.sin(math.pi / 4)
print(round(y, 2))

y = 1 / math.sqrt(2)
print(y)

print()

print('and:')
print(False and False)
print(False and True)
print(True and False)
print(True and True)
print()

print('or:')
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print()

print('not:')
print(not False)
print(not True)

print()

a = True
b = False
c = True
f = a and not b or c or (a and (b or c))
print(f)

print()

a = 5
b = 7

print(a < b)
print(b > 3)
print(a <= 8)
print(b >= 4)
print(a < 6 < b)
print(a == b)
print(a != b)
print(a is b)
print(a is not b)

x = "string"
y = x
z = input('Введите строку: ')
print(x is y)
print(z is x)

print()

a = "Привет"
b = 'Пока'
print(a, b)


c = str(8)
print(c)


d = """Lesson2. Variables and Data Types
Some data types explained in this lesson:
 - int
 - bool
 - float
 - complex
 - str
"""
print(d)


s = "привет \n пока "
e = "привет \\ пока"
r = "привет \" пока"
print(s)

print()

f = 'hel'
g = 'lo'
result = f + g
print(result)



a = 48
b = 73

m1 = '%d + %d = %d' % (a, b, a + b)
print(m1)

m2 = '{} - {} = {}'.format(a, b, a - b)
print(m2)

s = 'Hello, World!'


print(s[0])
print(s[4])
print(s[-1])

print(s[2:7])
print(s[2:7:2])

print(5, 1, 4, sep='; ')
print('he', 'llo', sep='')  #


print(5, end=' ')
print(27, end='\n\n')
print('he', end='')
print('llo')

s = input('Введите строку: ')
print('Вы ввели "', s, '"', sep='')


input()



n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))
print('{} + {} = {}'.format(n, m, n + m))



