def divide_numbers(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Please provide valid numeric values."


num1 = input("Enter the numerator: ")
num2 = input("Enter the denominator: ")


try:
    num1 = float(num1)
    num2 = float(num2)
    result = divide_numbers(num1, num2)
    print("Result of division:", result)
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print("An unexpected error occurred:", e)
