dic_things = {
"Юра": ("палатка", "рюкзак", "котелок"),
"Сергей": ("рюкзак", "палатка", "спички", "лопата"),
"Олег": ("стол", "рюкзак", "продукты"),
}
first = list(dic_things.keys())[0]
res = set(dic_things[first])
for k, v in dic_things.items():
    res = res.intersection(set(v))

print("У всех есть - ", *res)

dic_count = {}
for k, v in dic_things.items():
    for value in v:
        dic_count[value] = dic_count.get(value, 0) + 1
friends = len(list(dic_things.keys())) - 1
things = []
for k, v in dic_count.items():
    if v == friends:
        things.append(k)
for k, v in dic_things.items():
    for item in things:
        if item not in v:
            print(f"{item} нет у {k}!")
    break
one_thing = []
for k, v in dic_count.items():
    if v == 1:
        one_thing.append(k)
print("Вещи в единственном экземпляре: ", *one_thing)