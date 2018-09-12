print('Задание 1. Подготовка словаря')
print('------------------------------')
# f = open('cook_book.txt')
# print(f.read())
# print('Файл закрыт? {}'.format(f.closed))
# f.close()
# print('Файл закрыт? {}'.format(f.closed))
print('------------------------------')


cook_book = dict()
ingredients_list = list()

with open('cook_book.txt') as f:
    for line in f:
        dish = line
        number_of_ingredients = int(f.readline())
        i = 0
        for line in f:
            if i in range(number_of_ingredients):
                ingredient = line
                ingredients_list.append(ingredient)
                i += 1
        print('блюдо: ', dish, 'всего ингредиентов: ', number_of_ingredients, 'ингредиенты: ', ingredients_list)
        f.readline()