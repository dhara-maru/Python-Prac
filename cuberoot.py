def cube_root(x):
    return x**(1/3)


number = float(input("Enter a number: "))

result = cube_root(number)
print("The cube root of", number, "is:", result)
