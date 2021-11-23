def compare_num(num1:float, num2:float):
    # Params: num1 -> float, num2 -> float
    # Compares two numbers and returns the larger number
    # If equal, returns True
    pass

def add_num(num1:float, num2:float):
    # Params: num1 -> float, num2 -> float
    # Adds two numbers and returns value
    pass

def subtract_num(num1:float, num2:float):
    # Params: num1 -> float, num2 -> float
    # Subtracts two numbers and returns value
    pass

def multiply_num(num1:float, num2:float):
    # Params: num1 -> float, num2 -> float
    # Multiplies two nums and returns value
    pass

def divide_num(num1:float, num2:float):
    # Params: num1 -> float, num2 -> float
    # Divides two nums and returns value
    pass

def modulo_num(num1:float, num2:float):
    # Params: num1 -> float, num2: float
    # Modulos two nums and returns value
    pass

def get_average(*numbers) -> float:
    # Params: *numbers
    # Returns average of numbers
    
    total = 0
    number_elements = 0

    for numbers in numbers:
        total += numbers
        number_elements += 1
    
    return total / number_elements