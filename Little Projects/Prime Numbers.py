'''

Just a class to do with Prime Numbers, store Prime Number methods in here

'''

import time

import time


def is_prime(x):            # Method returns True or False based on whether or not the number passed in is a prime
    y = 2
    if x == 1:
        return False
    if x == 2:
        return True
    while y < x:
        if x % y == 0:
            y += 1
            return False
        else:
            y += 1
    return True

def slow_method():          # Iterates through numbers by 1 and prints the prime numbers within the range
    for i in range(1, 25000):
        if is_prime(i) is True:
            print(i)

def quicker_method():       # Quicker method of printing prime numbers below an upper number, based on 6n +/- 1
    n = 1
    print(2)
    print(3)
    print(5)
    while (6*n) + 1 < 20:
        if ((6*n) + 1) % 5 > 0:
            print((6*n) + 1)
        if ((6*n) - 1) % 5 > 0:
            print((6*n) - 1)
        n += 1

quicker_method()