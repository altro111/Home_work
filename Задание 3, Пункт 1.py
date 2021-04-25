def division(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return ('Деление на 0 запрещено')


num_1 = int(input('Введите первое число, которое хотите разделить: '))
num_2 = int(input('Введите второе число, на которое хотите разделить: '))

#Можно сделать валидацию по положительным числам или чтобы
#if num_1 and num_2 < 0:
#    print('введите положительные числа')
#else: print(division(num_1, num_2))
print(division(num_1, num_2))