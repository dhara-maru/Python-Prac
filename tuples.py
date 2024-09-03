empty_tuple = ()

my_tuple = (1, 2, 3, 'a', 'b', 'c')

another_tuple = 4, 5, 6

single_element_tuple = (42,)

print(my_tuple[0])
print(my_tuple[3])

subset_tuple = my_tuple[1:4]
print(subset_tuple)

# Uncommenting the line below will raise an error
# my_tuple[0] = 99

a, b, c = another_tuple
print(a, b, c)

print(len(my_tuple))

concatenated_tuple = my_tuple + another_tuple
print(concatenated_tuple)

repeated_tuple = my_tuple * 2
print(repeated_tuple)
