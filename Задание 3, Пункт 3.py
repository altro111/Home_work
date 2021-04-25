def sum_arg(num_1, num_2, num_3):
    return sum([num_1, num_2, num_3]) - min(num_1, num_2, num_3)


print(sum_arg(500, 100, 100))