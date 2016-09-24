# Project_Euler_Problem_6
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and
# the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the
# square of the sum.

import numpy
add_list = []

for i in range(0,101):
    add_list.append(i)

# sum of squares
sum_of_sq = numpy.array(add_list)**2
sosA = sum(sum_of_sq)

# square of sum
sq_of_sum = sum(add_list)
sosB = sq_of_sum **2

# get the difference
answer = sosB - sosA
print(answer)