#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Project 3
# Lab Section 206
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: python documentation, zyante exercises 1-8
#-------------------------------------------------------------------------------
# Comments and assumptions:
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
def odd_product(xs):
	#setting up list of odd numbers
	odd_list = []
	#making loop iterate for each value in xs
	for odd in xs:
		#checking if each value is divisible by 2
		if odd%2 != 0:
			#if so, value must be odd, add to oddlist
			odd_list.append(odd)
	#check if anything in oddlist
	if not odd_list:
		#if nothing in oddlist, set to 1
		num1 = 1
	#otherwise do this
	else:
		#sets first value to variable num1
		num1 = odd_list[0]

	#loop to iterate for each value in oddlist
	for num in odd_list[1:len(odd_list)]:
		#for each num, multiply to num1
		num1 *= num
	#return num1
	return num1

def divisors(n):
	#creating divisors list
	div_list = []
	#loop for each value between 1 and n
	for i in range(1, n+1):
		#check to see if divisible
		if n%i == 0:
			#add value to divisor list
			div_list.append(i)
	#return div list
	return div_list

def has_duplicates(xs):
	#make list for xs values
	xs_list = []
	#each value in xs
	for i in xs:
		#add it to xslist
		#basically, I'm splitting up xs
		#character by character
		xs_list.append(i)
		#y is the number of i in xs
		y = xs.count(i)
		#if there is more than 1 y
		if y >= 2:
			#therefore duplicates
			#therefore return true
			return True
	#if nothing matches, return false
	return False

def truncatable_prime(n):
	#variable i is false
	i = False
	#when i is false
	while i != True:
		#if n is 1 or negative
		if n <= 1:
			#not prime, return false
			return False
		#n is a single digit number
		if n < 10:
			#if n is 2
			if n == 2:
				#prime, return true
				return True
			#j in range 2 to n
			for j in range(2,n):
				#check if divisble
				if n % j == 0:
					#then its not prime
					#return false
					return False
				#otherwise
				else:
					#prime, return true
					return True
		#otherwise
		else:
			#k in range 2 to n
			for k in range(2,n):
				#if divisible by all k
				if n % k == 0:
					#not prime, return false
					return False
				#otherwise
				else:
					#continue running loop
					continue
		#truncate right most digit off n
		n = n // 10
	#returns false
	return False

def histogram(xs):
	#define ans variable as empty string
	ans = ''
	##loop for each value in list xs
	for i in range(len(xs)):
		#multiply o for value of xs
		os = 'o'*xs[i]
		#add os to ans
		ans = ans + os
		#check if last value in xs
		if i < (len(xs)-1):
			#add \n because its not
			ans = ans +'\n'
	#return ans
	return ans

def second_smallest(xs):
	#make list to store smallest values
	small_list = []
	#take first two values of xs and put them in smalllist
	small_list.extend([xs[0],xs[1]])
	#for each index in xs from 1 to end
	for i in range(1,len(xs)):
		#if the value of xs i is less than least value of smalllist
		if xs[i] < small_list[0]:
			#if value xsi is also smaller than 2nd value of slist
			if xs[i] < small_list[1]:
				#if slist0 bigger or equal to slist1
				if small_list[0] >= small_list[1]:
					#gets rid of slist0 and puts in xsi
					small_list[0] = xs[i]
				#otherwise, when slist 1 is bigger
				elif small_list[0] < small_list[1]:
					#get rid of slist1 and put in xsi
					small_list[1] = xs[i]
			#this checks for smaller numbers that are equal
			#example: 3 and 3 means 4 is not 2nd smallest
			#if xsi is same as slist1
			elif xs[i] == small_list[1]:
				#make slist0 as xsi
				small_list[0] = xs[i]
		#otherise checks if xsi is bigger than slist0
		elif xs[i] > small_list[0]:
			#if also bigger than slist1
			if xs[i] > small_list[1]:
				#no point, loop again
				continue
			#otherise if smaller than slist1
			elif xs[i] < small_list[1]:
				#get rid of slist1, make it xsi
				small_list[1] = xs[i]
		#if xsi is same as slist0
		elif xs[i] == small_list[0]:
			#xsi smaller than slist1
			if xs[i] < small_list[1]:
				#gets rid of slist 1, makes it xsi
				small_list[1] = xs[i]
	#end of for loop
	#checks if slist0 is bigger than slist1
	if small_list[0] > small_list[1]:
		#since 0 is second smallest, return slist0
		return small_list[0]
	#checks if s0 is smaller than s1
	elif small_list[0] < small_list[1]:
		#if s0 is smaller, return s1
		return small_list[1]
	#if they are equal
	elif small_list[0] == small_list[1]:
		#return the second one
		return small_list[1]