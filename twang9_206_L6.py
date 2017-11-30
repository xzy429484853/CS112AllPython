#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Lab 6
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
def show_time(hour,min):
	#if time is 0 hours
	if hour == 0:
		#if minutes less than two digits
		if min < 10:
			#format time in am, single digits
			time = "12:0{0}am".format(min)
		#otherwise
		else:
			#format time in am
			time = "12:{0}am".format(min)
	#check if hour is less than 12
	elif hour < 12:
		#if minutes less than two digits
		if min < 10:
			#format time in pm, single digits
			time = "{0}:0{1}am".format(hour,min)
		#otherwise
		else:
			##format time in am
			time = "{0}:{1}am".format(hour,min)
	#if the time is exactly 12 hours
	elif hour == 12:
		#if minutes less than two digits
		if min < 10:
			#format time in pm, single digits
			time = "{0}:0{1}pm".format(hour,min)
		#otherwise
		else:
			#format time in pm
			time = "{0}:{1}pm".format(hour,min)
	#check if time is 12 or more but less than 24
	elif hour > 12 and hour < 24:
		#get the non military value of hour
		hour -=12
		#if minutes less than two digits
		if min < 10:
			#format time in pm, single digits
			time = "{0}:0{1}pm".format(hour,min)
		#otherwise
		else:
			#time is in pm format
			time = "{0}:{1}pm".format(hour,min)
	#returning the time
	return time

def split_up(funds,people):
	#divide funds by people, funds per person
	each = funds / people
	#using % to fill in the number of people and the amount for each person
	per_each = "each person (of %d) gets $%.2f as their share" % (people,each)
	#return the string per each
	return per_each

def border_msg(msg):
	#set finalmsg as empty string
	final_msg = ''
	#split up message
	split_msg = msg.split('\n')
	#check for longest line
	#set line split to zero
	line_split = 0
	#for loop to find longest element of splitmsg
	for i in range(len(split_msg)):
		#if bigger than current value
		if len(split_msg[i]) > line_split:
			#then replace
			line_split = len(split_msg[i])
		#otherwise
		else:
			#keep going in the loop
			continue
	#set border length
	#find amount of rows needed
	height = len(split_msg)
	#add one space on each side of width
	line_split += 2
	#create top boundary line, set to finalmsg
	final_msg = final_msg + '+' + ('-'*line_split) + '+\n'
	#for each row in message
	for j in range(height):
		#set finalmsg to centered splitmsg
		final_msg=final_msg+'|'+"{0:{fill}{align}{width}}".format \
		(split_msg[j],fill='',align ='^',width=line_split)+'|'+'\n'
	#create bottom boundary, set to finalmsg
	final_msg = final_msg + '+' + ('-'*line_split) + '+' + '\n'
	#return final msg
	return final_msg

