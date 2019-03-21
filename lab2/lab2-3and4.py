#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)

from cs50 import get_int

x = get_int("Input x: ")
y = get_int("Input y: ")

while y==0:
    y = get_int("Y cannot be 0, try again: ")

print('X is divisible by Y' if x % y == 0 else 'X is not divisible by Y')

#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)

print(f"{x/y:.2f}")