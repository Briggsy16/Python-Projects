'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

# Started on 27th March 2015 15:25 PM
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

done = False

while True:
    x = 2
    count = 0
    prime_number = 10001
    while True:
        if is_prime(x) is True:
            count += 1
            if count == prime_number:
                print(x)
                break
            x += 1
        else:
            x += 1
    break



end_time = time.clock()
total_time = end_time - start_time
print('This took ' + str(total_time) + ' seconds to complete')

# Completed using Brute Force 27th March 2015 15:46 PM (Solution takes 96 seconds)

