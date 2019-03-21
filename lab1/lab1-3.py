#3 write a function which takes an array of numbers as an input and finds the lowest value.
#Return the index of that element and its value (1p)

def min_val(l):

    x = l[0]
    indexes = []
    for i in range(0, len(l)):
        if l[i] < x:
            x = l[i]
    for i in range(0, len(l)):
        if l[i] == x:
            indexes.append(i)

    return indexes, x