empty_dict = {}

my_dict = {'key1': 'value1', 'key2': 2, 'key3': [3, 4, 5]}

another_dict = {'key4': 'value4', 'key5': 6}

print(my_dict['key1'])
print(my_dict['key3'])

my_dict['key2'] = 99
print(my_dict)

my_dict['key6'] = 'value6'
print(my_dict)

del my_dict['key1']
print(my_dict)

keys = list(my_dict.keys())
print(keys)

values = list(my_dict.values())
print(values)

items = list(my_dict.items())
print(items)

merged_dict = {**my_dict, **another_dict}
print(merged_dict)

my_dict.update(another_dict)
print(my_dict)
