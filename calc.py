#calculator version 1.0
#Tony Wang

#setting up input variables
user_var1 = 0
user_var2 = 0
new_answer = 0

print('A)Addition')
print('B)Subtraction')
print('C)Multiplication')
print('D)Division')
print('E)Power')
print('F)Exit')

#calculation loop commence
while True:
	print('use x if you want to use the previous calculation as a number')
	start_var = input('Please input the first letter of the mathmatical process you want to do: ')
	if start_var == 'a':
		#add
		while True:
			user_var1 = (input('First number: ')
			
			if isinstance(user_var1, int)
				int(user_var1)
				
			if user_var1 == 'x':
				user_var1 == new_answer
				
			elif user_var1 != 'x':
				print('unreadable value')
				continue
			#end if-state, continue to var2
			break
		while True:
			user_var2 = input('Second number: ')
			
			if isinstance(user_var2, int):
				int(user_var2)
				
			if user_var2 == 'x':
				user_var2 == new_answer
				
			elif user_var2 != 'x':
				print('unreadable value')
				continue
			break
			#end if-state, continue to calc
		new_answer = user_var1+user_var2
		print(new_answer)
		#end calc
		
		print("done")
	if start_var == 'b':
		#subtract
		user_var1 = float(input('First number: '))
		user_var2 = float(input('Second number: '))
		new_answer = user_var1-user_var2
		
		print("done")
	if start_var == 'c':
		#multiply
		user_var1 = float(input('First number: '))
		user_var2 = float(input('Second number: '))
		new_answer = user_var1*user_var2
		
		print("done")
	if start_var == 'd':
		#divide
		user_var1 = float(input('First number: '))
		user_var2 = float(input('Second number: '))
		new_answer = user_var1/user_var2
		
		print("done")
	if start_var == 'e':
		#power
		user_var1 = float(input('First number: '))
		user_var2 = float(input('Second number: '))
		new_answer = user_var1**user_var2
		
		print("done")
	if start_var == 'f':
		#exit
		print("done")
		exit()
	elif (start_var != 'a' and start_var != 'b' and start_var != 'c' and start_var != 'd' and start_var != 'e' and start_var != 'f'):
		#in case of unreadable command
		print('Command error')
		continue
print("loop complete")