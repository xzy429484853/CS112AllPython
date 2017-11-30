#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Lab 7
# Lab Section 206
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: python documentation, zyante exercises 1-9
#-------------------------------------------------------------------------------
# Comments and assumptions:
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
def rank3(x,y,z, ascending=True):
	#put x y z into ranklist
	rank_list = [x,y,z]
	#sort rank_list with .sort()
	rank_list.sort()
	#check if ascending is false
	if ascending == False:
		#reverse the order of ranklist
		rank_list.reverse()
	#return a tupled version of ranklist
	return tuple(rank_list)
	
def remove(val, xs, limit=None):
	#count number of val in xs, set to countx
	countx = xs.count(val)
	#if limit doesn't exist
	if limit == None:
		#as long as countx is greater than or equal to 1
		while countx >= 1:
			#take out first instance of val
			xs.remove(val)
			#recount countx
			countx = xs.count(val)
	#if limit isn't none
	elif limit != None:
		#see if limit is bigger than countx
		if limit > countx:
			#while countx is greater than or equal to 1
			while countx >= 1:
				#remove first instance val from xs
				xs.remove(val)
				#recount countx
				countx = xs.count(val)
		#otherwise
		else:
			#while limit is non negative and less than countx
			while 0 < limit <= countx:
				#remove first instance of val
				xs.remove(val)
				#recount countx
				countx = xs.count(val)
	#return xs
	return xs

def filter_chars(msg, keeps = None):
	#make new string to empty string
	new_string = ''
	#if no keeps
	if keeps == None:
		#split msg by spaces
		new_string = msg.split(' ')
		#then join all parts of new_string together
		new_string = ''.join(new_string)
		#then slice from beginning to index 7
		new_string = new_string[:7]
	#otherise
	else:
		#for i in msg
		for i in range(len(msg)):
			#if msg[i] matches keeps
			if msg[i] in keeps:
				#add msg[i] to newstinrg
				new_string += msg[i]
	#return newstring
	return new_string

def relocate_evens(data = [], new_home = None):
	#if new_home is none
	if new_home == None:
		#make newhome empty list
		new_home = []
	#for i in data
	for i in data:
		#if i is even
		if i % 2 == 0:
			#attach to newhome
			new_home.append(i)
			#remove from data
			data.remove(i)
	#return newhome
	return new_home
