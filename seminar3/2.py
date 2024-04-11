tup = (12, "line 1", "line 2", 26.13, 1522, "line 3")
dic_type = {}
for item in tup:
    t = type(item).__name__
if t not in dic_type:
    dic_type[t] = []
dic_type[t].append(item)
print(dic_type)