import os

cook_book = {}
# ingredients_list = []

with open('cookBook.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        ingredients_list = []
        dish = line.strip()
        ingredient_quantity = int(f.readline())
        for ingredients in range(ingredient_quantity):
            ingredient = f.readline()
            ingredient_name, quantity, measure = ingredient.strip().split(' | ')
            ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            dish_compisit = {dish: ingredients_list}
        empty_string = f.readline()
        cook_book.update(dish_compisit)

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] not in ingredient_list:
                    ingredient_list[ingredient["ingredient_name"]] = {'measure': ingredient['measure'], 'quantity': (int(ingredient['quantity']) * person_count)}
                else:
                    ingredient_list[ingredient["ingredient_name"]]['quantity'] += (int(ingredient['quantity']) * person_count)
    print(ingredient_list)
get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 4 )

all_text = './Text/'
files_all = []
for filename in os.listdir(all_text):
    if filename.endswith(".txt"):
        with open(all_text + filename, 'r', encoding='utf-8') as f:
            text = f.readlines()
            len_ = len(text)
            info_file = [len_, filename, text]
            files_all.append(info_file)

with open('Sorted.txt', 'w', encoding='utf-8') as f:
    for output in sorted(files_all):
        f.write(f'{output[1]} \n {output[0]} \n {" ".join(output[2])} \n')
        f.write(f'\n')

with open('Sorted.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())