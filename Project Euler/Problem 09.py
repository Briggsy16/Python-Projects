'''

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

# Started on 29th March 2015 14:11 PM

import time
start_time = time.clock()

a = 1
b = 2
c = 3

def pythag_theory(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

while a < 1000:
    while b < 1000:
        while c < 1000:
            if pythag_theory(a, b, c) is True and a + b + c == 1000:
                print(a)
                print(b)
                print(c)
                print('---------')
                c += 1
            else:
                c += 1
        c = b + 1
        if pythag_theory(a, b, c) is True and a + b + c == 1000:
            print(a)
            print(b)
            print(c)
            print('---------')
            b += 1
        else:
            b += 1
    b = a + 1
    if pythag_theory(a, b, c) is True and a + b + c == 1000:
        print(a)
        print(b)
        print(c)
        print('---------')
        a += 1
    else:
        a += 1




end_time = time.clock()
total_time = end_time - start_time
print('This took ' + str(total_time) + ' seconds to complete')

# Completed on 2nd April 2015 14:44 PM
# Brute force method - 168 seconds
