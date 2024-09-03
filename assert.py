def divide_numbers(x, y):
    assert y != 0, "Error: Cannot divide by zero."
    return x / y

num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))


try:
    result = divide_numbers(num1, num2)
    print("Result of division:", result)
except AssertionError as e:
    print(e)
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print("An unexpected error occurred:", e)
