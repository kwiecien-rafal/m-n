#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)

from cs50 import get_int

x = get_int("Input x:")
while x%2!=0:
    x = get_int("X has to be an even integer, x: ")
y = get_int("Input y: ")
while  y%2!=0 or y==0 or x%y!=0:
    y = get_int('Y has to be an even integer, not 0, and be x\'s devider, y: : ')

print(x,'/',y,'=',x//y)