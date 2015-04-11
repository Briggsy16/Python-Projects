"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

# Started on 25th March 2015 19:33 PM

import time

start_time = time.clock()

def is_palindrome(x):                           # Function to determine if number passed in is a palindrome
    y = str(x)                                  # Converts number to a string
    if len(y) == 6 or 7:                        # Checks if length of string is 6 or 7
        if y[0] == y[len(y)-1]:
            if y[1] == y[len(y)-2]:
                if y[2] == y[len(y)-3]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    if len(y) == 3:                             # Checks if length of string is 3
        if y[0] == y[len(y)-1]:
            return True
        else:
            return False
    if len(y) == 4 or 5:                        # Checks if length of string is 4 or 5
        if y[0] == y[len(y)-1]:
            if y[1] == y[len(y)-2]:
                return True
            else:
                return False
        else:
            return False


first_number = 100                              # First number of multiplication
palindromes = []
lower_range = 100                               # Lowest 3 digit number
upper_range = 999                               # Highest 3 digit number

while first_number < 1000:
    for i in range(lower_range, upper_range):   # Checks through the number range
        number = first_number * i
        if is_palindrome(number) is True:       # Checks if product of the two numbers is a palindrome
            palindromes.append(number)          # If the number is a palindrome, appends it to a list.
    first_number += 1                           # Adds one to the value of first_number

print(max(palindromes))                         # Prints largest palindrome found

end_time = time.clock()
total_time = end_time - start_time
print('This took ' + str(total_time) + ' seconds to complete')

# Completed on 26th March 2015 15:05 PM