# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

#через список
seasons = ['зима', 'весна', 'лето', 'осень']
month = int(input("Введите месяц по номеру "))
if month >=13 or month <=0:
    print("Месяц должен быть между 1 и 12")
else:
    if month == 12 or month == 1 or month == 2:
        print(seasons[0])
    elif 3 <= month <= 5:
        print(seasons[1])
    elif 6 <= month <= 8:
        print(seasons[2])
    elif 9 <= month <= 11:
        print(seasons[3])

#Через словарь
seasons = { 1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month = int(input("Введите месяц по номеру "))
if month >=13 or month <=0:
    print("Месяц должен быть между 1 и 12")
else:
    if month == 12 or month == 1 or month == 2:
        print(seasons.get(1))
    elif 3 <= month <= 5:
        print(seasons.get(2))
    elif 6 <= month <= 8:
        print(seasons.get(3))
    elif 9 <= month <= 11:
        print(seasons.get(4))