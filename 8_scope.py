# Global variable
global_variable = 10

def example_function():
    # Local variable
    local_variable = 5
    print("Inside the function: global_variable =", global_variable)
    print("Inside the function: local_variable =", local_variable)

# Call the function
example_function()

# Accessing global variable outside the function
print("Outside the function: global_variable =", global_variable)

# print("Outside the function: local_variable =", local_variable)
