
i = 6
while i > 0 :
    print(i)
    i -= 1

S = 0
while S != "ку":
    S = input("введите ку :")

print('От 1 до 5:')
n = 1
while True:
    print(n)
    n += 1
    if n == 6:
        break

while True:
    print("you got 50 damage while you are not use your spell")
    print("""your spells :
         -fire
         -ice
         -dark
         -light
         -froze
         -lava
         """)
    spell = input("choice your spell :")

    if spell == "fire" or spell == "ice" or spell == "dark" or spell == "light" or spell == "froze" or spell == "lava":
        print("you win this fight!")
        break

i = 1
while i < 10:
    i += 1

    if i == 6 :
        continue
    print(i)

attempts_left = 4
while attempts_left > 0 :
    attempts_left -= 1
    password = input("Введите пароль :")
    if password == "123456789" :
        print('Вы ввели правильный пароль. Доступ разрешен!')
        break
    else:
        print("Вы ввели не верный пароль.\nУ вас осталось попыток - {} .".format(attempts_left))


for i in range(1,10):
    print(i)

for a in range(1,10,2):
    for i in range(20):
        if i >= 1:
            print(":)",end = "")
        elif i >= 10:
            print(":(", end="")
        else:
            print(":0", end = "")

    print()



