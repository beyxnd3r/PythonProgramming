menu = [
["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]
pizza = menu[0][0]
salad = menu[1][0]
soup = menu[2][0]
print(f"Вот наше меню:{pizza}, {salad},{soup}. Ингридиенты какого блюда хотите узнать(а также цену). Или можете изменить цену?")
ro = input("Узнать ингридиенты или изменить цену?")
if ro == "Изменить" or ro == "изменить":
    ing = input("Блюдо:")
    price = input("Цена:")
    if ing == pizza:
        menu[0][2] = price
        print("Новая цена:", menu[0][2])
    elif ing == salad:
        menu[1][2] = price
        print("Новая цена:", menu[1][2])
    elif ing == soup:
        menu[2][2] = price
        print("Новая цена:", menu[2][2])

if ro == "Узнать" or ro == "узнать":
    ing = input("Блюдо:")
    if ing == pizza:
        print("Пожалуйста, вот ингридиенты с ценой:", menu[0][1][0],menu[0][1][1],menu[0][1][2],menu[0][1][3])
        print(menu[0][2])
    elif ing == salad:
        print("Пожалуйста, вот ингридиенты с ценой:", menu[1][1][0], menu[1][1][1], menu[1][1][2], menu[1][1][3])
        print(menu[1][2])
    elif ing == soup:
        print("Пожалуйста, вот ингридиенты с ценой:", menu[2][1][0], menu[2][1][1], menu[2][1][2], menu[2][1][3])
        print(menu[2][2])



