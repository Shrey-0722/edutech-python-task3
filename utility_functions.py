# Global Variable
import _sitebuiltins
company_name = "Edutech Solution"


# Basic Functions with Return Type
def add_numbers(a, b):
    return a + b


#Basic Functions with Default Parameters
def greet_user(name="Shrey"):
    return f"Hello, {name}"


#Using *args 
def calculate_sum(*numbers):
    total = sum(numbers)
    return total


#Using **kwargs
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    


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

# Output
print("Addition of 5 and 3:", add_numbers(5, 3))
print()

print(greet_user("Shrey"))
print()

print("Sum of 11, 10:", calculate_sum(11, 10))
print()

student_info(name="Shrey", age=20, city="Surat")
print()

print("Square of 5:", square(5))
print("Product of 4 and 6:", multiply(4, 6))
print()

print(local_scope_example())
print("Company Name (Global Variable):", global_scope_example())
print()
