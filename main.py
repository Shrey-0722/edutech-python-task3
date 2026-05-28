# Global Variable
company_name = "Edutech Solution"


# Basic Functions with Return Type
def add_numbers(a, b):
    return a + b


#Basic Functions with Default Parameters
def greet_user(name="Student"):
    return f"Hello, {name}!"


#Using *args for Variable Number of Arguments
def calculate_sum(*numbers):
    total = sum(numbers)
    return total


#Using **kwargs for Keyword Arguments
def profile_user(**kwargs):
    name = kwargs.get('name', 'Unknown')
    age = kwargs.get('age', 'Unknown')
    city = kwargs.get('city', 'Unknown')
    return f"Name: {name}, Age: {age}, City: {city}"


#Using Lambda Functions
square = lambda x: x * x
multiply = lambda x, y: x * y


#Local Scope Example
def local_scope_example():
    message = "This is a local variable"
    return message

#Global Scope Example
def global_scope_example():
    global company_name
    return company_name

#Function Returning Multiple Values
def multiple_returns(a, b): 
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    return sum_result, diff_result, prod_result

#Recursive Function Example
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Main Program
print("Addition of 5 and 3:", add_numbers(5, 3))
print()

print(greet_user())
print()

print(greet_user("Shrey"))
print("Sum of 1, 2, 3, 4:", calculate_sum(1, 2, 3, 4))
print()

print(profile_user(name="Shrey", age=20, city="Surat"))
print()

print("Square of 5:", square(5))
print("Product of 4 and 6:", multiply(4, 6))
print()

print(local_scope_example())
print("Company Name (Global Variable):", global_scope_example())
print()

sum_result, diff_result, prod_result = multiple_returns(10, 5)
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print()

print("Factorial of 5:", factorial(5))
