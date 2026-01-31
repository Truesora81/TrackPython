import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    summ = []

    for item in data:
        item_sum = item['score'] * item['weight']
        item['sum'] = item_sum
        summ.append(item_sum)

    return round(sum(summ), 3)

print(task())