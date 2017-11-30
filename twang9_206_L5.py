#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Lab 5
# Lab Section 206
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: python documentation excercises in online book up to chapter 7.
#-------------------------------------------------------------------------------
# Comments and assumptions:
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
def location(xs, key):
	#setting up the variable
	index = 0
	#make loop, iterate each num in xs
	for (index, value) in enumerate(xs):
		#checks if value of key exists in xs
		if key == value:
			#returns index of the value
			return index
		#checks if it doesn't
		if key != value:
			#continues loop
			continue
	#checks if value and key don't equal
	if index != key:
		#then returns None becasuse key didn't
		#exists in xs
		return None

def fibonacci(n):
	#make fib list, default numbers to start
	#off with because need at least 2 numbers
	#for equation to begin
	fib = [1,1]
	#iterates each number up to n-1
	for i in range(n-1):
		#less than index of 2 check, because 
		#starting numbers are already in fib list
		if n < 2:
			#returns the function
			break
		#n greater than or equal to index of 2
		elif n >= 2:
			#sets f = to last two numbers sum
			f = fib[-1] + fib[-2]
			#add f to end of fib list
			fib.append(f)
	#returns the last value in fib list		
	return fib[-1]

def int_sqrt(n):
	#make list to store all squares
	sqrt_list = []
	#check each number up to n
	for i in range(1,n):
		#check if square goes over n
		if i*i <= n:
			#if not, add to list
			sqrt_list.append(i)
		#when square finally goes over
		elif i*i > n:
			#break out of loop
			break
	if not sqrt_list:
		return 1
	#returns the last value of sqrtlist
	return sqrt_list[-1]

def sum_evens_2d(xss):
	#creating list for indexes
	dex_list = []
	#creat list of even nums
	even_list = []
	#setting variable sum-total to 0
	sum_total = 0
	#for loop and enumerate to get indexes and values
	for (index, value) in enumerate(xss):
		#for each index, add to index list
		dex_list.append(index)
	#loop through all indexes in xss
	for index in range(len(xss)):
		#for each value of xss, index it
		value = xss[index]
		#for every value from xss
		for each in value:
			#divide by 2 to check for remainder
			if each%2 == 0:
				#when no remainder, add to even list
				even_list.append(each)
	#check each index in even_list
	for index in range(len(even_list)):
		#for each value in even list
		value = even_list[index]
		#add that to the sum_total
		sum_total += value
	#return sum_total as answer
	return sum_total
