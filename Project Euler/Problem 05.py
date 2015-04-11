'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

# Started on 26th March 2015 15:12 PM

import time

start_time = time.clock()


def brute_force():              # Takes 45 seconds
    is_divisible = False
    start_number = 20
    while is_divisible is False:
        if start_number % 20 == 0:
            if start_number % 19 == 0:
                if start_number % 18 == 0:
                    if start_number % 17 == 0:
                        if start_number % 16 == 0:
                            if start_number % 15 == 0:
                                if start_number % 14 == 0:
                                    if start_number % 13 == 0:
                                        if start_number % 12 == 0:
                                            if start_number % 11 == 0:
                                                if start_number % 10 == 0:
                                                    if start_number % 9 == 0:
                                                        if start_number % 8 == 0:
                                                            if start_number % 7 == 0:
                                                                if start_number % 6 == 0:
                                                                    if start_number % 5 == 0:
                                                                        if start_number % 4 == 0:
                                                                            is_divisible = True
                                                                            print(start_number)
                                                                        else:
                                                                            start_number += 1
                                                                    else:
                                                                        start_number += 1
                                                                else:
                                                                    start_number += 1
                                                            else:
                                                                start_number += 1
                                                        else:
                                                            start_number += 1
                                                    else:
                                                        start_number += 1
                                                else:
                                                    start_number += 1
                                            else:
                                                start_number += 1
                                        else:
                                            start_number += 1
                                    else:
                                        start_number += 1
                                else:
                                    start_number += 1
                            else:
                                start_number += 1
                        else:
                            start_number += 1
                    else:
                        start_number += 1
                else:
                    start_number += 1
            else:
                start_number += 1
        else:
            start_number += 1

def brute_force2():             # Takes 2.8 seconds
    is_divisible = False
    start_number = 20
    while is_divisible is False:
        if start_number % 20 == 0:
            if start_number % 19 == 0:
                if start_number % 18 == 0:
                    if start_number % 17 == 0:
                        if start_number % 16 == 0:
                            if start_number % 15 == 0:
                                if start_number % 14 == 0:
                                    if start_number % 13 == 0:
                                        if start_number % 12 == 0:
                                            if start_number % 11 == 0:
                                                is_divisible = True
                                                print(start_number)
                                            else:
                                                start_number += 12
                                        else:
                                            start_number += 13
                                    else:
                                        start_number += 14
                                else:
                                    start_number += 15
                            else:
                                start_number += 16
                        else:
                            start_number += 17
                    else:
                        start_number += 18
                else:
                    start_number += 19
            else:
                start_number += 20
        else:
            start_number += 1

brute_force2()

end_time = time.clock()
total_time = end_time - start_time
print('This took ' + str(total_time) + ' seconds to complete')

# Completed on 26th March 2015 15:40 PM