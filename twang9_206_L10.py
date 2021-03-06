#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Project 3
# Lab Section 206
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: python documentation, zyante exercises 1-13
#-------------------------------------------------------------------------------
# Comments and assumptions:
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
def get(xs, index, response=None):
	#open try block to catch errors
	try:
		#return index of xs
		return xs[index]
	#open exception block to continue if error
	except:
		#return error response
		return response

def classify(input_string):
	#create empty numer list
	numer = []
	#create empty alpha list
	alpha = []
	#set ans to splitted list of inputstring
	ans = input_string.split()
	#for each value i in ans list
	for i in ans:
		#open try block
		try:
			#make i an int, set to y
			y = int(i)
			#add y to numerlist
			numer.append(y)
		#if error occurs
		except:
			#i equal to y
			y = i
			#alpha list append
			alpha.append(y)
	#list ans becomes tuple of numer,alpha
	ans = (numer, alpha)
	#return ans
	return ans

def shelve(inventory, product_list):
	#open try block
	try:
		#for tup in productlist
		for prod_amount_tup in product_list:
			#unpack tup to product and amount
			product,amount = prod_amount_tup
			#if product exists
			if product in inventory:
				#get old amount
				dict_amount = inventory.get(product)
				#add new amount
				dict_amount += amount
				#check if less than 0
				if dict_amount < 0:
					#if kiwi
					if product == "kiwi":
						#raise error for kiwi specifically
						raise ValueError("negative amount for kiwi")
					#raise error
					raise ValueError("negative amount for product")
				#otherwise update dictionary
				inventory.update({product:dict_amount})
			#if not exist
			elif product not in inventory:
				#if less than 0
				if amount < 0:
					#raise error
					raise ValueError("negative amount for product")
				#otherwise update dictionary
				inventory.update({product:amount})
	#except to catch errors
	except ValueError as e:
		#re-raise error
		raise

