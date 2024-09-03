empty_list = []

my_list = [1, 2, 3, 'a', 'b', 'c']

another_list = [4, 5, 6]

single_element_list = [42]

print(my_list[0])
print(my_list[3])

subset_list = my_list[1:4]
print(subset_list)

my_list[0] = 99

my_list.append('d')
print(my_list)

a, b, c = another_list
print(a, b, c)

print(len(my_list))

concatenated_list = my_list + another_list
print(concatenated_list)

repeated_list = my_list * 2
print(repeated_list)
