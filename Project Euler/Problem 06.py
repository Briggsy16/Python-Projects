'''

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

# Started on 27th March 2015 15:10 PM

import time
start_time = time.clock()


def sum_of_square(lower_range, upper_range):
    sum = 0
    for i in range(lower_range, upper_range):
        sum += i**2
    return sum


def square_of_sum(lower_range, upper_range):
    sum = 0
    for i in range(lower_range, upper_range):
        sum += i
    square = sum**2
    return square



x = sum_of_square(1, 101)
y = square_of_sum(1, 101)
print(y - x)

end_time = time.clock()
total_time = end_time - start_time
print('This took ' + str(total_time) + ' seconds to complete')

# Completed on 27th March 2015 15:22 PM
