# Complete the function that takes a single list of numbers. Your function must return the sum of the even values of this list.

# Only numbers without decimals like 4 or 4.0 can be even.

# The input is a sequence of numbers: integers and/or floats.

# [4, 1, 5, 10, 7, 9, 8]  -->  30   # because 4 + 2 + 10 + 6 + 8 = 22
# []                               -->  0
# [4.0, 6.6, 2] --> 6.0 because 4.0 + 2 = 6.0

list1 = [4, 1, 5, 10, 7, 9, 8]

def evenAddition(n):
    new = []
    for i in n:
        if i % 2 == 0:
            new.append(i)
            
    out = sum(new)
    return out

print(evenAddition(list1))