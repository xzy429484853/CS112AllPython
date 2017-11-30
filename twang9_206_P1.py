#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Project 1
# Lab Section 206
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Online Textbook sections 1 and 2
#-------------------------------------------------------------------------------
# Comments and assumptions: N/A
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
#Welcoming the user to the store
print('Welcome to the School Supplies Store!')

#Asking for user's name by asking for user input and storing in a variable
name_var = input('What is your name? ')

#Asking for how much of each product user desires
#Pencils
num_pencil = int(input('How many 29-cent pencils do you want? ')) 
#Sheafs of graphpaper
num_graph = int(input('How many 200-cent sheafs of graph paper do you want? '))
#Scantrons
num_scantron = int(input('How many 45-cent scantrons do you want? '))

#Calculating total cost, multiplying data variables by cost, add together
total_cost = (num_pencil*29)+(num_graph*200)+(num_scantron*45)

#Printing total cost to user
print('Total cost:', total_cost, 'cents')

#Asking for payment in cents by user input, storing in a variable
pay_cents =(int(input('How many cents are you paying with? ')))

#Calculating the gross change, payment subtracted by cost
total_change = (pay_cents - total_cost)

#Making change by currency type, storing in variables
#Using floor divison and remainder divison to separate currency types
change_dollars = (total_change//100) #Dollars
change_quarters = ((total_change%100)//25) #Quarters
change_dimes = (((total_change%100)%25)//10) #Dimes
change_nickels = ((((total_change%100)%25)%10)//5) #Nickels
change_pennies = ((((total_change%100)%25)%10)%5) #Pennies

#Printing change breakdown to user
print('Your change is', total_change, 'cents:') #Total change
print(change_dollars, 'dollars') #Dollars
print(change_quarters, 'quarters') #Quarters
print(change_dimes, 'dimes') #Dimes
print(change_nickels, 'nickels') #Nickels
print(change_pennies, 'pennies') #Pennies

#Thanking the user for his business
print('Thank you,', name_var +'!')
