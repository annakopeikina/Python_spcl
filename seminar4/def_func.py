def no_return(data: list[int]):
        for i, item in enumerate(data):
                data[i] = item + 1
        print(f'In func {data =  }') 


my_list = [2, 4, 6, 8]
print(f'In main {my_list =  }')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')

'''
def from_one_to_n(n, data=[]):
        for i in range(1, n + 1):
                data.append(i)
        return data
new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')
'''
def from_one_to_n(n, data=None):
        if data is None:
                data = []
        for i in range(1, n + 1):
                data.append(i)                   
        return data
new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')