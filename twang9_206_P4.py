#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Project 3
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
#1
def read_coords(s):
	#outer is row, inner is columns for that row
	#gstring is final answer string form
	gstring_coords = []
	#working list
	rawstring_list = []
	#splitting by the white spaces, \n lines are ignored in this case
	rawstring_list = s.split()
	#for i in range of len of rawstring
	for i in range(len(rawstring_list)):
		#for j in range of len of rawstringi
		for j in range(len(rawstring_list[i])):
			#if O or .
			if rawstring_list[i][j] == '.' or rawstring_list[i][j] == 'O':
				#if alive
				if rawstring_list[i][j] == 'O':
					#append to gstring
					gstring_coords.append((i,j))
				#otherwise
				else:
					#keep going
					continue
			#if not O or .
			else:
				#something wrong, return none
				return None
	#if len of rows are not same
	if len(rawstring_list[0]) != len(rawstring_list[-1]):
		#return none
		return None
	#return gstringcoords
	return gstring_coords
#2
def get_dimensions(s):
	# . for dead cell, O for living cell, grid
	#set dim_grid to none
	dim_grid = None
	#rawstring to empty list
	rawstring_list = []
	#row to 0
	grid_row = 0
	#col to 0
	grid_col = 0
	#splitting by the white spaces, \n lines are ignored in this case
	rawstring_list = s.split()
	#this loop checks each row for appriate length
	#for i in range of len of rawstring
	for i in range(len(rawstring_list)):
		#if initial rawstring doesnt equal rawstringi
		if len(rawstring_list[0]) != len(rawstring_list[i]):
			#grid size off, return none
			return None
		#if not, grid + 1
		grid_row += 1
	#for j in range of len of rawstringi
	for j in range(len(rawstring_list[i])):
		#if rawstringij is O or .
		if rawstring_list[i][j] == '.' or rawstring_list[i][j] == 'O':
			#add 1 to gridcol
			grid_col += 1
		#if not
		else:
			#return none
			return None
	#return row,col
	return (grid_row,grid_col)
#3
def build_empty_grid(height, width):
	#empty grid to empty
	empty_grid = []
	#working list to empty
	temp_list = []
	#if height and width both positive
	if height > 0 and width > 0:
		#for i in range of width
		for i in range(width):
			#add false value to working list
			temp_list.append(False)
		#for j in range height
		for j in range(height):
			#make copy to copy of working list
			copy = temp_list[:]
			#add copy to emptygrid
			empty_grid.append(copy)
	#return empty grid
	return empty_grid
#4
def build_grid(s):
	#set coords to result of read_coords
	coords = read_coords(s)
	#set height, row to get_dimensions
	height, row = get_dimensions(s)
	#set egrid to result of build_empty_grid
	egrid = build_empty_grid(height, row)
	#empty list coord_list
	coord_list = []
	#for i in coords
	for i in coords:
		#make j and k to i
		j,k = i
		#set coordinate in egrid of jk to True
		egrid[j][k] = True
	#return egrid
	return egrid
#5
def show_grid(grid, live='O', dead='.'):
	#grid_to_string as empty string
	grid_to_string = ''
	#for i in range of len of grid
	for i in range(len(grid)):
		#for j in range of len of gridi
		for j in range(len(grid[i])):
			#if ij is false
			if grid[i][j] == False:
				#its dead, add dead to gridtostring
				grid_to_string += dead
			#if ij is true
			elif grid[i][j] == True:
				#its alive, add alive to gridtostring
				grid_to_string += live
			#otherwise
			else:
				#return none
				return None
		#add newline break at the end of loop
		grid_to_string += '\n'
	#return gridtostring
	return grid_to_string
#6
def count_living(grid):
	#livingcells to 0
	living_cells = 0
	#for i in range of len of grid
	for i in range(len(grid)):
		#for i in range of len of gridi
		for j in range(len(grid[i])):
			#if ij is True
			if grid[i][j] == True:
				#livingcells add 1
				living_cells += 1
	#return livingcells
	return living_cells
#7
def any_living(grid):
	#for i in range of len grid
	for i in range(len(grid)):
		#for j in range of len of gridi
		for j in range(len(grid[i])):
			#if ij is True
			if grid[i][j] == True:
				#return true
				return True
	#if no living, return false
	return False
#8
def on_grid(grid, r, c):
	#if r or c is negative
	if r < 0 or c < 0:
		#return false
		return False
	#set stringofgrid to show_grid
	string_of_grid = show_grid(grid)
	#set x,y to get_dimensions
	x,y = get_dimensions(string_of_grid)
	#if x bigger or equal to r and y bigger than or equal to c
	if r >= x or c >= y:
		#return False
		return False
	#otherwise return True
	return True
#9
def count_neighbors(grid, r, c):
	#r-1[c-1,c,c+1], r[c-1,c+1], r+1[c-1,c,c+1]
	#set alive_neighbors to 0
	alive_neighbors = 0 
	#make list of rows to check
	rows = [r-1,r,r+1]
	#make list of columns to check
	columns = [c-1,c,c+1]
	#for i in rows
	for i in rows:
		#for j in columns
		for j in columns:
			#if coord is r,c dont eval, keep going
			if i == r and j == c:
				#keep going
				continue
			#otherwise
			else:
				#set on_some to on_grid i,j
				on_some = on_grid(grid, i,j)
				#if it is true
				if on_some == True:
					#set ans_some to the coordinate in grid
					ans_some = grid[i][j]
					#if ans_some is true
					if ans_some == True:
						#add 1 to alive_neighbors
						alive_neighbors +=1
					#otheriwse
					else:
						#keep going
						continue
				#otherwise
				else:
					#keep going
					continue
	#return aliveneighbors
	return alive_neighbors
#10
def next_gen(grid):
	#get string of grid
	string_of_grid = show_grid(grid)
	#get dimensions of grid
	height, width = get_dimensions(string_of_grid)
	#make empty copy of grid
	copy_grid = build_empty_grid(height, width)
	#for i in range of len of grid
	for i in range(len(grid)):
		#for j in range of len of gridi
		for j in range(len(grid[i])):
			#set aliveneighbors to count_neighbors with ij
			alive_neighbors = count_neighbors(grid, i, j)
			#if ij is false
			if grid[i][j] == False:
				#if aliveneighbors is 3
				if alive_neighbors == 3:
					#set copygridij to True
					copy_grid[i][j] = True
				#otherwise
				else:
					#set copygridij to false
					copy_grid[i][j] = False
			#otherwise ij is True
			elif grid[i][j] == True:
				#if aliveneighbors is less than 2 or greater than 3
				if alive_neighbors < 2 or alive_neighbors > 3:
					#set copygridij to false
					copy_grid[i][j] = False
				#otherwise
				else:
					#set copygridij to true
					copy_grid[i][j] = True
	#return copy_grid
	return copy_grid
#11
def n_gens(grid, n=20):
	#set listofgens to empty list
	list_of_gens = []
	#set templist to given grid
	temp_list = grid
	#for i in range of n
	for i in range(n):
		#add templist to listofgens
		list_of_gens.append(temp_list)
		#calculate new templist with next_gen
		temp_list = next_gen(temp_list)
	#return listofgens
	return list_of_gens
#12
def is_still_life(grid, limit=100):
	#for i in range of the limit
	for i in range(limit):
		#set checkgenslist to n_gens of the grid and limit
		check_gens_list = n_gens(grid,limit)
		#if limit less than 2
		if limit < 2:
			#return false
			return False
		#if i is not equal to i-1
		if check_gens_list[i-1] == check_gens_list[i]:
			#return True
			return True
		#otherwise if i-1 is not equal to i-2
		elif check_gens_list[i-1] == check_gens_list[i-2]:
			#return True
			return True
		#otherwise
		else:
			#return False
			return False
#13
def is_cycle(grid, limit=100):
	#set checkgenslist to n_gens
	check_gens_list = n_gens(grid,limit)
	#for j in checkgenslist
	for j in check_gens_list:
		#count each value of j in checkgenslist set to y
		y = check_gens_list.count(j)
		#if y - limit is exactly 0
		#check if everything is the same
		if y - limit == 0:
			break
		#otherwise if y is more or equal to 2
		elif y >= 2:
			#and limit greater than 3
			if limit > 3:
				#but if checkgenslisti is same as checkgenslisti-1
				if check_gens_list[limit-1] == check_gens_list[limit-2]:
					break
			#otherwise return True
			return True
	#if none of that, return False
	return False
