import copy

enemy = {
    'Color': 'Yellow',
    'Health': 100,
    'Skills': ['One','Two','three']
}
all_enemy = []

for i in range(10):
    all_enemy.append(copy.deepcopy(enemy))

all_enemy[5]['Health'] = 50
all_enemy[5]['Skills'].append('Four')

for en in all_enemy:
    print(en)
