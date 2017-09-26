#Problem #3: What is the largest prime factor of the number 600851475143?
#Instead of starting from the top, start from the bottom!!!
question = 13195 #Set this to number in question
x= 1
done= False

def factor_check(number): #Checks to see if a prime number is a factor
    if question % number == 0:
        is_factor= True
    else:
        is_factor= False
    return is_factor

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

while x < question:
    factor = factor_check(question-x)
    if factor == True:
        is_prime= prime_check(question-x)
        if is_prime == True:
            break
    x += 1
