"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Started on 25th March 2015 18:37 PM

import time

start_time = time.clock()


def is_prime(x):
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

def is_prime_2(x):
    if x % 2 == 0:
        return False
    elif x % 3 == 0:
        return False
    elif x % 5 == 0:
        return False
    elif x % 7 == 0:
        return False
    return True

# print(is_prime(9))

x = 1
count = 0
while x < 600851475143:
    if is_prime(x) is True:
        if 600851475143 % x == 0:
            print(x)
        x += 1
    else:
        x += 1

end_time = time.clock()
print(end_time - start_time)

# Completed on 25th March 2015 18:56 PM