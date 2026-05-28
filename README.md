# Edutech Solution Python Development Internship - Task 3: Functional Programming

## Final Outcome
A Python script (`main.py`) containing various functions that implement:
- Functions with return types
- Functions with default parameters
- Variable number of arguments using `*args`
- Keyword arguments using `**kwargs`
- Lambda functions
- Global and Local scope examples
- Functions returning multiple values
- Recursive functions

## Interview Questions & Deliverables

### 1. What are Lambda functions?
Lambda functions, also known as anonymous functions, are small, one-line functions in Python that are defined without a name. They are created using the `lambda` keyword instead of the standard `def` keyword. They can take any number of arguments but can only have one expression. They are typically used for short, simple operations where a full function definition is unnecessary.

**Example used in the script:**
```python
square = lambda x: x * x
```

### 2. Global vs Local Scope?
- **Local Scope:** Variables created inside a function belong to the local scope of that function and can only be accessed inside that function.
- **Global Scope:** Variables created in the main body of the Python code are global variables and belong to the global scope. They can be accessed from anywhere in the code, both inside and outside of functions. To modify a global variable inside a function, the `global` keyword must be used.

**Example used in the script:**
`company_name` is defined globally and accessed via the `global` keyword, while the `message` variable is defined locally inside the `local_scope_example()` function.

## How to Run
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the script using Python:
   ```bash
   python main.py
   ```

## Code Implementation (`main.py`)
```python
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
```

## Output
```text
Addition of 5 and 3: 8

Hello, Student!

Hello, Shrey!
Sum of 1, 2, 3, 4: 10

Name: Shrey, Age: 20, City: Surat

Square of 5: 25
Product of 4 and 6: 24

This is a local variable
Company Name (Global Variable): Edutech Solution

Sum: 15
Difference: 5
Product: 50

Factorial of 5: 120
```

### Submitted By 
Shrey Gamit
P.P Savani University
CSE