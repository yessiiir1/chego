#Создание игрового персонажа


name = input("Введите имя персонажа : ")
print(name, ",Добро пожаловать в редактор персонажа. ")


print()
floor = 0
while (floor != "male" or floor != "female"):
    floor = input("выберите пол персонажа(male/female) :")

    if floor == 'male':
        print('выбран пол персонажа, мужской.')
    elif floor == 'female':
        print('выбран пол персонажа, жениский.')
    else:
        print('вы не выбрали пол персонажа. Введите male или female.')


print()

string = """Доступные расы: 
- Эльф
- Друид
- Человек
- Орк
- Нелюдь
- Каджит"""
print(string)

species = input("Выберите расу :")










