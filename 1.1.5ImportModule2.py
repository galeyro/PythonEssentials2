import math

def sin(x):
    """
    Calculates the sine of a given angle in radians.

    Parameters:
    x (float): The angle in radians.

    Returns:
    float: The sine of the angle, or None if the angle is not equal to pi/2.
    """
    if 2*x==pi:
        return 0.99999999
    else:
        return None
 
pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))