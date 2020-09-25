## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	numbers = x.split("/")
	
	# Check for zero denominator and zero numerator

	if numbers[0] == "0": return "0"
	if numbers[1] == "0": return "Undefined"

	# converts negative denominator to positive and transfer it to numerator
	# eliminate negative sign if both the numerator and denominator are negative

	if (int(numbers[1]) < 0):
		numbers = [-1 * int(x) for x in numbers]

	# generate unique set of common factor of the numerator and the denominator

	common_factor = set(factors(numbers[0])) & set(factors(numbers[1]))

	# check for common factors and get the highest common factor
	# divide the give fractions with highest common factor and return the results

	if common_factor:
		highest_common_factor = max(common_factor)
		return "{}/{}".format(int(numbers[0]) // highest_common_factor, int(numbers[1]) // highest_common_factor )

	# if nothing is found about the numbers, return them as the are given
	
	return "{}/{}".format(numbers[0], numbers[1])



def factors(x):
	
	# ###########################################################################
	# A function that generate the factors of any number
	# It accept a number
	# Returns a list of factors or empty list if there are no factors 
	# ###########################################################################
	
	# converts the given number to integer
	num = abs(int(x))
	return [i for i in range(1, num+1) if not num % i]


print(lowest_terms("20/10"))
print(lowest_terms("16/28"))
print(lowest_terms("-50/25") )
print(lowest_terms("20/-60") )
print(lowest_terms("-300/165") )
print(lowest_terms("-12/-26"))
print(lowest_terms("90/0") )
print(lowest_terms("0/12") )
