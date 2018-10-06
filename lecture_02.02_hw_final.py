from pprint import pprint

cook_book = dict()
ingredient = dict() #словарь отдельного ингредиента (ключи: наименование, количество, ЕИ ингредиента)
# ingredients = list() - элементы словаря (список словарей с детальной информацией по каждому отдельному ингредиенту)
# ingredient_details = list() - список свойств ингредиента (наименование / количество / ЕИ)

with open('cook_book.txt', encoding='utf-8') as f:
    for line in f:
        dish = line.strip()
        # print(dish)
        ingredients_qt = f.readline().strip()
        q = int(ingredients_qt)
        ingredients = list()
        k = 0
        for i in range(q):
            item = f.readline().strip()
            ingredient_details = item.split(' | ')
            ingredient['ingridient_name'] = ingredient_details[0]
            ingredient['quantity'] = ingredient_details[1]
            ingredient['measure'] = ingredient_details[2]
            k += 1
            ingredients.append(ingredient.copy())
        cook_book[dish] = ingredients
        f.readline()
    pprint(cook_book)
    pprint(ingredients)


def get_shop_list_by_dishes():
    person_count = int(input('Введите количество персон:'))
    purchase_list = dict()
    for dish, ingredients in cook_book.items():
        for item in ingredients:
            meas_quant = dict()
            name = item.get('ingridient_name')
            meas_quant['measure'] = item.get('measure')
            meas_quant['quantity'] = int(item.get('quantity')) * person_count
            if name not in purchase_list:
                purchase_list[name] = meas_quant
            else:
                purchase_list[name]['quantity'] += meas_quant['quantity']
    pprint(purchase_list)
