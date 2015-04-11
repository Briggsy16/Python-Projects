"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

# Started on 25th March 2015

import time

start_time = time.clock()

def sum_of(x):
    number = 0
    count = 0
    while number < x:
        if number % 3 == 0:
            count += number
        elif number % 5 == 0:
            count += number
        else: print(number)
        number += 1
    return count

print(sum_of(1000))
end_time = time.clock()
print(end_time - start_time)
# Completed using brute force 25th March 2015 18:15 PM