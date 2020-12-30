#Exercise 1

list_solyanka = ['user', 2, 45.3, None, [1, 2], 3, 9]
for element in list_solyanka:
    print(type(element))

#Exercise 2
i = 0
if (len(list_solyanka) % 2) == 0:
    while i < len(list_solyanka):
        list_solyanka[i], list_solyanka[i + 1] = list_solyanka[i + 1], list_solyanka[i]
        i += 2
else:
    while i < len(list_solyanka)-1:
        list_solyanka[i], list_solyanka[i + 1] = list_solyanka[i + 1], list_solyanka[i]
        i += 2
print(list_solyanka)

#Exercise 3
seasons_list = ["winter", "Spring", "summer","autumn"]
print("Input number of month (1-12): ")
month = int(input())
season = (month//3)%4
print(seasons_list[season])

seasons_dict = {"1": "winter", "2": "winter","3": "Spring", "4": "Spring", "5": "Spring",
        "6": "summer","7": "summer","8": "summer","9":"autumn","10":"autumn","11":"autumn", "12": "winter"}
print("Input number of month (1-12): ")
month = input()
print(seasons_dict.get(month))

#Exercise 4
print("Input some words: ")
phrase = input()
words = phrase.split(" ")
i = 1
for word in words:
    if len(word) > 10:
        word = word[0:9]
    print(f"{i}. {word}")
    i += 1

#Exercise 5

raiting = [7, 5, 3, 3, 2]
while True:
    print("Input number or end: ")
    str = input()
    if str == "end":
        break
    else:
        number = int(str)
        i=0
        # Мне только кажется, или следующая строка пахнет как-то не так?
        while i < len(raiting) and number <= raiting[i]:
            i += 1
        print(i)
        raiting.insert(i,number)
        print(raiting)
print(f"Final raiting is {raiting}")

#Exercise 6

products = []
i = 1
while True:
    print("Input name of product or end: ")
    name = input()
    if name == "end":
        break
    else:
        print("Input price of product: ")
        price = int(input())
        print("Input quantity of product: ")
        quantity = int(input())
        print("Input measure unit of product: ")
        unit = input()
        product = (i, {"name": name, "price": price, "quantity": quantity, "measure": unit})
        products.append(product)
        i += 1
print(products)