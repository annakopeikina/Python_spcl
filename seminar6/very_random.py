import random as rnd

print(f'{rnd.random() = }')
rnd.seed(33)
state = rnd.getstate()
print(f'{state = }')
print(f'{rnd.random() =}')
print(f'{rnd.random() =}')
rnd.setstate(state)
print(f'{rnd.random() =}')
print(f'{rnd.random() =}')

# randint(a, b)  целое число от а до b 
# unioform(a, b) Вещественное число от а до b
# choice(a, b) случайный элемент последовательности
# randrange(start,stop[,step]) Число из диапазона
# shuffle(x) перемешиваем коллекцию x in place
# sample(population,k,*,counts=None) Выборка в k элементов из population
START = -100
STOP = 1000
STEP = 10
data =[2,4,6,8,42,73]


print(f'{rnd.randint(START, STOP) =}')
print(f'{rnd.uniform(START, STOP) =}')
print(f'{rnd.choice(data) =}')
print(f'{rnd.randrange(START, STOP, STEP) =}')

print(f'{data = }')
rnd.shuffle(data)
print(f'{data =}')

print(f'{rnd.sample(data,3) =}')
print(f'{rnd.sample(data, 3, counts=[1,1,1,1,1,100]) =}')