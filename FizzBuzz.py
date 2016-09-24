"""FizzBuzz in Python 3 by Karl Daniti
Task:
Write a program that prints the integers from   1   to   100   (inclusive).


But:

  for multiples of three,   print   Fizz     (instead of the number)
  for multiples of five,   print   Buzz     (instead of the number)
  for multiples of both three and five,   print   FizzBuzz     (instead of the number) """

for n in range(0,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
