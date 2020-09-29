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

	highest_common_factor = max(set(factors(numbers[0])) & set(factors(numbers[1])))
	return "{}/{}".format(int(numbers[0]) // highest_common_factor, int(numbers[1]) // highest_common_factor )




def factors(x):
	"""
	# ###########################################################################
	# A function that generate the factors of any number
	# It accept a number
	# Returns a list of factors or empty list if there are no factors 
	#
	# input: x
	# return: list of factors of x
	# ###########################################################################
	"""

	# converts the given number to integer
	num = abs(int(x))
	return [i for i in range(1, num+1) if not num % i]

