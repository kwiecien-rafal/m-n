#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
import numpy as np
from cs50 import get_float

x = get_float("Input x: ")
while x<=0:
    x = get_float("Try again, x: ")
y = get_float("Input y: ")
while y<=0:
    y = get_float("Try again, y: ")

print(f"Perimeter of circle with radius x: {x*2*np.pi:.2f}, field: {np.pi*x**2:.2f}")
print(f"Perimeter of circle with radius y: {y*2*np.pi:.2f}, field: {np.pi*y**2:.2f}")