#Problem 1. Find the sum of all multiples of 3 o 5 below 1000
total= 0
for number in range(1,1000):
    if number % 3 == 0:
        total += number
    elif number % 5 == 0:
        total += number
print total
