"""Json_и_функциональный_стиль_программирования_9"""

import json

data = str()
with open('animals.json', mode='r') as f:
    data = f.read()
data = json.loads(data)

print('Информация о всех птицах:')
bird = list(filter(lambda x: x['animal_type'] == 'Bird', data))
print(bird)

print('Кол-во дневных животных:')
day = list(filter(lambda x: x['active_time'] == 'Diurnal', data))
print(len(day))

print('Животное с наименьшим весом:')
min_weight = min(data, key=lambda x: x['weight_min'])
print(min_weight['name'])
