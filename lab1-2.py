#2 ask the user for a number and print its factorial (1p)

x = 0
while x <= 0 or x % 1 != 0:
    x = float(input("Input a number: "))

x = int(x)
fact = 1
for i in range(fact, x + 1):
    fact = fact * i

print(fact)
