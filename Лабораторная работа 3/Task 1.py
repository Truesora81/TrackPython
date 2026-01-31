
def get_item_index(items_list, item):
    return items_list.index(item) if item in items_list else None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in list(set(['банан', 'груша', 'персик'])):
    index_item = get_item_index(items_list, find_item)
    if index_item is not None:
        print(f'Первое вхождение товара {find_item} имеет индекс {index_item}.')
    else:
        print(f'Товар {find_item} не найдет в списке.')