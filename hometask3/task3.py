# Создайте словарь со списком вещей для похода в качестве ключа и их массой 
#в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную 
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

items = {
    'палатка': 2.5,
    'спальный мешок': 1.8,
    'кастрюля': 0.7,
    'фляга': 0.2,
    'еда (на 1 день)': 0.5,
    'карта': 0.1,
    'фонарик': 0.3,
    'переносной газовый горелка': 0.6,
    'фляга с водой': 1.0,
    'первая помощь': 0.5,
    'зажигалка': 0.1,
    'нож': 0.3,
    'антидот от ФОС (anti-venom)': 0.2
}
def generate_inventory(max_capacity):
    inventory = []
    current_weight = 0
    sorted_items = sorted(items.items(), key=lambda x: x[1])
# lambda  это способ создания анонимных (безымянных) функций в Python. 
# Вместо определения функции с помощью ключевого слова def, можно использовать lambda,
# чтобы создать функцию "на лету".
# lambda arguments: expression
# __arguments__ - это аргументы функции (может быть любое количество, но только одно выражение);
# __expression__ - выражение, которое будет выполнено функцией.
# В представленном коде lambda используется внутри функции sorted для определения ключа 
# сортировки. Он принимает каждый элемент items.items() (который представляет собой пары 
# ключ-значение из словаря items), и сортирует их по значению (массе вещи) в порядке 
# возрастания.
# sorted_items = sorted(items.items(), key=lambda x: x[1])
# Здесь lambda x: x[1] создает анонимную функцию, которая принимает один аргумент x 
#(каждую пару ключ-значение из словаря) и возвращает x[1] (значение, то есть массу вещи).
# Это позволяет sorted отсортировать элементы словаря items по значению (массе) в порядке
# возрастания.

    for item, weight in sorted_items:
        if current_weight + weight <= max_capacity:
            inventory.append(item)
            current_weight += weight

    return inventory

max_capacity = 5.0 
print(generate_inventory(max_capacity))


from itertools import combinations
def generate_all_combinations(max_capacity):
    all_combinations = []

    # Генерируем все возможные комбинации вещей
    for i in range(1, len(items) + 1):
        for combo in combinations(items.items(), i):
            weight_sum = sum(weight for item, weight in combo)
            if weight_sum <= max_capacity:
                all_combinations.append([item for item, weight in combo])

    return all_combinations

max_capacity = 5.0  # Пример максимальной грузоподъемности рюкзака
for combination in generate_all_combinations(max_capacity):
    print("•", combination)


