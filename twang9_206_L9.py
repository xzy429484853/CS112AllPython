#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Project 3
# Lab Section 206
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: python documentation, zyante exercises 1-12
#-------------------------------------------------------------------------------
# Comments and assumptions:
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
#1
def counts(xs):
	#empty dict ans
	ans = {}
	#for value in list xs
	for i in xs:
		#count how many i and set to val
		val = xs.count(i)
		#temp dict work with i: val
		work = {i:val}
		#add work dict to ans dict
		ans.update(work)
	#return ans dict
	return ans
	
def weeklies(plants_d):
	#empty list week_list
	week_list = []
	#for key and value in dict plants_d
	for key, value in plants_d.items():
		#if value is weekly
		if value == 'weekly':
			#add key to week_list
			week_list.append(key)
	#sort weeklist and make it ans
	ans = sorted(week_list)
	#return ans
	return ans
	
def closest(d, what, here):
	#placeholder value sofar
	so_far = 50
	#ans as none
	ans = None
	#for key and value in d dict
	for key, value in d.items():
		#if value is same as what
		if value == what:
			#unpack tuple key
			x2, y2 = key
			#unpack tuple here
			x1, y1 = here
			#distance equation
			eq = (((x2-x1)**2)+((y2-y1)**2))**0.5
			#check if distance is less than placeholder
			if eq < so_far:
				#if less, make eq new sofar
				so_far = eq
				#make ans the key of the eq
				ans = key
	#return ans
	return ans
	
def file_counts(filename):
	#set empty list open_list
	open_list = []
	#open filename as myfile
	myfile = open(filename)
	#for each line in myfile
	for line in myfile:
		#add the line as int to open_list
		open_list.append(int(line))
	#in_file_count to counts of open_list
	in_file_count = counts(open_list)
	#return in_file_count
	return in_file_count