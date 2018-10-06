from pprint import pprint

def get_shop_list_by_dishes():
  cook_book = dict()
  ingredient = dict()
  with open('cook_book.txt', encoding='utf-8') as f:
    for line in f:
        dish = line.strip()
        ingredients_qt = f.readline().strip()
        q = int(ingredients_qt)
        ingredients_list = list()
        while len(ingredients_list) <= (q-1):
            item = f.readline().strip()
            ingredients_list.append(item)
        k = 0
        ingredients = list()
        for item in ingredients_list:
            ingredient_details = ingredients_list[k].split(' | ')
            ingredient['наименование'] = ingredient_details[0]
            ingredient['количество'] = ingredient_details[1]
            ingredient['ЕИ'] = ingredient_details[2]
            k += 1
            ingredients.append(ingredient.copy())
        cook_book[dish] = ingredients
        f.readline()
    pprint(cook_book)
    person_count = int(input('Введите количество персон:'))
    purchase_list = dict()
    for dish, ingredients in cook_book.items():
        iter = 0
        for item in ingredients:
            meas_quant = dict()
            ingredient = ingredients[iter]
            name = ingredient.get('наименование')
            meas_quant['ЕИ'] = ingredient.get('ЕИ')
            meas_quant['количество'] = int(ingredient.get('количество'))*person_count
            if name not in purchase_list:
                purchase_list[name] = meas_quant
            else:
                qt = purchase_list[name]['количество']
                purchase_list[name]['количество'] = qt + meas_quant['количество']
            iter += 1
    pprint(purchase_list)
