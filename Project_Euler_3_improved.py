#Problem #3: What is the largest prime factor of the number 600,851,475,143?
#Instead of starting from the top, start from the bottom!!!
import math
question = 600851475143 #Set this to number in question
done= False

def factor_check(number): #Checks to see if a prime number is a factor
    if question % number == 0:
        return True
    else:
        return False

def prime_check(factor): #Checks to see if a factor is prime
	x = factor/2
	prime= True
	while prime == True and x>1:
		if factor % x == 0:
			prime = False
		elif x == 2:
			print str(factor) + " is prime"
		x -= 1
	return prime

def finding_highest_prime_factor(question): #finds highest prime factor
    x= 0
    while x < question:
        factor = factor_check(int(math.sqrt(question))-x)
        if factor == True:
            is_prime= prime_check(int(math.sqrt(question))-x)
            if is_prime == True:
                break
        x += 1

print "Prime Check: " + str(prime_check(29))
print "Factor Check: " + str(factor_check(29))
print finding_highest_prime_factor(question)
