def pr(l):
    for i in range(l):
        print(i)

x = int(input("Enter a number :"))
pr(x)

def hello_world():
    print('Hello, World!')

hello_world()

print_numbers = None
def main():
    a = int(input('Введите a: '))
    print_numbers(a)

main()

def main():
    print('Hello, World!')

if __name__ == 'main':
    main()

def numbers(a, b):
    return a + b
x = numbers(1,2)
print(x)

def procedure():
    print('всем ку')

procedure()

def func(x):
    if x > 0:
        return x / 5
    else:
        return x * -1

def main():
    for i in range(-3, 4):
        y = func(i)
        print( i, y)

if __name__ == '__main__':
    main()

def hello(name):
    if not name:
        return
    print('Hello, ', name, "!")

hello('Ivan')
hello('')
hello('What are you doing?')

def add(a, b):
    return a * b

def sub(a, b):
    return a * b

print(add(10, 5) / sub(1, 5))

def info(a, b, c):
    print('Курс :',a )
    print('Направление :',b )
    print('Впечатление :',c )
    print()

info(1, "11.05.01","Очень круто!" )

info(a = 1,b = "11.05.01",c = "Замечательно!")

def hello(n='my name'):
    print('Hello, ', n, '!')

hello('Ivan')
hello()