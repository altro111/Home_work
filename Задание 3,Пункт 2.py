def user(**kwargs):
    return kwargs


# Еще вариант с лямбда
#user_2 = lambda **kwargs: kwargs

print(user(Имя='Сергей', Фамилия='Кукушкин', Год_рождения=1983, Город='Подольск', email='Alro29@yandex.ru'))
#print(user_2(Имя='Сергей', Фамилия='Кукушкин', Год_рождения=1983, Город='Подольск', email='Alro29@yandex.ru'))
