
#-------------------------------------------------------------------------------

# TASK 0 (example)

# EXAMPLE: this function is implemented for you, to show 
# what a function definition looks like, and how the
# 'student' added four lines to complete the definition.

def is_even(n):
	# at the end, we'll return whatever current value
	# that's in ans as our return value. Somewhere in 
	# this function, you should re-assign it to be
	# either True or to False.
	ans = None

	# make decisions with if-else structures to determine
	# whether n is even (divisible by two) or not. Then,
	# set ans to equal True or equal False as your answer.
	
	# YOUR CODE GOES HERE. (Since it's an example, we've
	# already written "your code" - four lines).

	if n % 2 == 0 :
		print("Is Even")
		ans = True
	else:
		print("Is Odd")
		ans = False
		
	# make this the last line of your function definition
	return ans

#-------------------------------------------------------------------------------

# TASK 1

# given a non-negative integer, this function returns a
# string (it does not print!) matching the letter grade
# for our class (check the syllabus).
def letter_grade(score):
	# starting value for variable ans. Change it before
	# the end of the function.
	ans = ""
	
	# YOUR CODE GOES HERE. Figure out what string you want
	# to assign to the ans variable, and assign it.
	if score >= 98:
		ans = 'A+'
	elif score >= 92:
		ans = 'A'
	elif score >= 90:
		ans = 'A-'
	elif score >= 88:
		ans = 'B+'
	elif score >= 82:
		ans = 'B'
	elif score >= 80:
		ans = 'B-'
	elif score >= 78:
		ans = 'C+'
	elif score >= 72:
		ans = 'C'
	elif score >= 70:
		ans = 'C-'
	elif score >= 60:
		ans = 'D'
	elif score < 60:
		ans = 'F'
	elif score == 0:
		ans = 'Error'
	
	# leave this as the last line of your function.
	return ans

#-------------------------------------------------------------------------------

# TASK 2

# without calling the max(), min(), or any sorting functionality,
# this function determines the two largest values of the three 
# and returns their sum. The integers might be negative. When
# there's a tie between two numbers, it doesn't actually matter
# which one you choose.

def sum2biggest(a, b, c):
	# starting value for variable ans. Replace it with the
	# actual answer integer before reaching the return stmt.
	ans = None
	
	# find the sum of the two largest values. Re-assign the
	# answer to the ans variable.
	# YOUR CODE GOES HERE

	if a >= c and a >= b:
		if b >= c:
			ans = a + b
		elif b < c:
			ans = a + c
	elif b >= c and b >= a:
		if a >= c:
			ans = a + b
		elif a < c:
			ans = b + c
	elif c >= a and c >= b:
		if a >= b:
			ans = a + c
		elif a < b:
			ans = b + c
	
	# leave this as the last line of your function.
	return ans

#-------------------------------------------------------------------------------

	