import math

def print_math_module_attributes():
    """
    Prints the attributes of the math module.
    """
    for name in dir(math):
        print(name, end="\n")

print_math_module_attributes()

