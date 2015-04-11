'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

# Started on 2nd April 2015 14:46 PM

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


def quick_method():
    n = 1
    sum_of = 10
    number = 0
    max_limit = 2000000
    while number < max_limit:
        if ((6*n) + 1) % 5 > 0:
            sum_of += (6*n) + 1
            number = (6*n) + 1
            if number > max_limit:
                sum_of -= (6*n) + 1
        if ((6*n) - 1) % 5 > 0:
            sum_of += (6*n) - 1
            number = (6*n) - 1
            if number > max_limit:
                sum_of -= (6*n) - 1
        n += 1


def slow_method():
    number = 1
    max_limit = 2000000
    sum_of = 0
    while number < max_limit:
        if is_prime(number) is True:
            sum_of += number
        number += 1
    print(sum_of)

slow_method()

end_time = time.clock()
total_time = end_time - start_time
print('This took ' + str(total_time) + ' seconds to complete')