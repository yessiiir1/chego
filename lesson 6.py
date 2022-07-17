"""
Док строка
"""

def fc():
    """Типо комментарий, но документационная строка(((
    """
    print('))))')

fc()
print(fc.__doc__)

help(fc)
help(print)

a = int(input('Введите число: '))
print('Двоичная система:         ', bin(a))
print('Восьмеричная система:     ', oct(a))
print('Шестнадцатеричная система:', hex(a))

l = int(input("Enter a number :"))
for i in reversed(range(l)):
    print(i)

a = 5
b = 2
c = 12
print(min(a, b, c))
print(max(a, b, c))


def outer():
    def inner():
        print('Внутренняя функция')

    print('Внешняя функция')
    inner()

outer()

def func():
    print(a)

a = 'глобальная переменная'
func()

def func():
    a = 'локальная переменная'
    print(a)

a = 'глобальная переменная'
func()
print(a)

def func():
    global a
    print(a)
    a = 'новое значение'
    print(a)

a = 'глобальная переменная'
func()
print(a)

def function(c, d):
    global a, b
    a = 12
    b = 7
    c = 10
    d = 12

a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)
function(c, d)
print(a, b, c, d)

def outer():
    a = 443

    def inner():
        nonlocal a
        print(a)
        a = 123323

    print(a)
    inner()
    print(var)

a = 123
print(a)
outer()
print(a)


def outer():
    a = 84

    def inner():
        global a
        print(a)  #
        a = 100

    print(a)
    inner()
    print(a)


a = 20
print(a)
outer()
print(a)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

index = int(input('Введите номер числа Фибоначчи: '))
print(fib(index))

def hanoi(n, a, b, c):
    if n != 0:
        hanoi(n - 1, a, c, b)
        print('Перенести кольцо из', a, 'в', c)
        hanoi(n - 1, b, a, c)

hanoi(3, 'A', 'B', 'C')