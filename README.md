# Edutech Solution Python Development Internship - Task 3: Functional Programming

## Final Outcome
- Functions
- Functions with return types
- Functions with default parameters
- Variable number of arguments using *args
- Keyword arguments using *kwargs
- Lambda functions
- Global and Local scope examples


## Interview Questions & Deliverables

### 1. What are Lambda functions?
Lambda functions, also known as anonymous functions, are small, one-line functions in Python that are defined without a name. They are created using the `lambda` keyword instead of the standard `def` keyword. They can take any number of arguments but can only have one expression. They are typically used for short, simple operations where a full function definition is unnecessary.

**Example used in the script:**
```python
square = lambda x: x * x
```

### 2. Global vs Local Scope?
**Local Scope:** Variables created inside a function belong to the local scope of that function and can only be accessed inside that function.

**Global Scope:** Variables created in the main body of the Python code are global variables and belong to the global scope. They can be accessed from anywhere in the code, both inside and outside of functions. To modify a global variable inside a function, the `global` keyword must be used.

## Code Implementation (`utility_functions.py`)
```python
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

```

## Output
```text
Addition of 5 and 3: 8

Hello, Shrey


Sum of 11, 10: 21

name: Shrey
age: 20
city: Surat

Square of 5: 25
Product of 4 and 6: 24

This is a local variable
Company Name (Global Variable): Edutech Solution

```

### Submitted By 
Shrey Gamit
