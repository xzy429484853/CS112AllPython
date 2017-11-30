# STUDENTS: TO USE:
# 
# The following command will test all test cases on your file:
# 
#   python3 <thisfile.py> <your_one_file.py>
# 
# 
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1, func2, and func3, run this command:
# 
#   python3 <thisfile.py> <your_one_file.py> func1 func2 func3
# 


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
#    follow a convention: to test a function named foobar, the test must be
#    named "test_foobar_#", where # may be any digits at the end, such as
#    "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS. Do not include any
#   unofficial helper functions. If you want to make helper definitions
#   to use while testing, those can also be added there for clarity.
# 
# # TO IMPLEMENT (not yet a feature):
# to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
# 
# A work in progress by Mark Snyder, Oct. 2015.

import unittest
import shutil
import sys
import os
import time
import importlib

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
	
REQUIRED_DEFNS = ["Tile","Direction","TileError","Puzzle",
				  'UP','DOWN','LEFT','RIGHT','dirs']

# things inside of classes that we also want to use as test names (the classes' methods)
SUB_DEFNS = ["display","find_opening","move","is_solved","scramble","extra_credit"]

RENAMED_FILE = "student"

# END SPECIALIZATION SECTION
############################################################################
############################################################################


#BEGIN EXTRAS SECTION

# grabs a flat list of the values of the tiles in a puzzle.
def puzzvals(p):
	vals = []
	for row in p.grid:
		for tile in row:
			vals.append(tile.value)
	return vals

def swaptiles(p, locA, locB):
	(ar, ac) = locA
	(br, bc) = locB
	
	# remove tile A, put anything in as a placeholder
	tileA = p.grid[ar].pop(ac)
	p.grid[ar].insert(ac, "dummyA")
	
	# remove tile B, put anything in as a placeholder
	tileB = p.grid[br].pop(bc)
	p.grid[br].insert(bc, "dummyB")
	
	# put tileA where tileB was.
	p.grid[br].pop(bc)
	p.grid[br].insert(bc,tileA)
	
	# put tileB where tileA was.
	p.grid[ar].pop(ac)
	p.grid[ar].insert(ac,tileB)
	

# END EXTRAS SECTION

############################################################################
############################################################################



# enter batch mode by giving a directory to work on.
BATCH_MODE = (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))



# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):
	
	
	#---------------------------------------------------------------------
	
	# class Tile
	
	def test_Tile_1(self): t = Tile(10);   self.assertEqual(t.value,10)
	def test_Tile_2(self): t = Tile(None); self.assertEqual(t.value,None)
	def test_Tile_3(self): t = Tile(10);   self.assertEqual(str(t),"10")
	def test_Tile_4(self): t = Tile(4);    self.assertEqual(str(t)," 4")
	def test_Tile_5(self): t = Tile(None); self.assertEqual(str(t),"<>")
	def test_Tile_6(self): t = Tile(10);   self.assertEqual(repr(t),"Tile(10)")
	def test_Tile_7(self): t = Tile(None); self.assertEqual(repr(t),"Tile(None)")
	
	#---------------------------------------------------------------------
	
	# class Direction
	
	# due to testing weight, some of these that could have been individual tests have been combined.
	
	def test_Direction_1(self): d = Direction("UP");    self.assertEqual(d.value,"UP")
	def test_Direction_2(self): d = Direction("DOWN");  self.assertEqual(d.value,"DOWN")
	def test_Direction_3(self):
		d = Direction("LEFT")
		self.assertEqual(d.value,"LEFT")
		d = Direction("RIGHT")
		self.assertEqual(d.value,"RIGHT")
	
	def test_Direction_4(self):
		d = Direction("UP")
		self.assertEqual(str(d),"UP")
		d = Direction("DOWN")
		self.assertEqual(str(d),"DOWN")
	def test_Direction_5(self):
		d = Direction("LEFT")
		self.assertEqual(str(d),"LEFT")
		d = Direction("RIGHT")
		self.assertEqual(str(d),"RIGHT")
	
	def test_Direction_6(self):
		d = Direction("UP")
		self.assertEqual(repr(d), "Direction('UP')")
		d = Direction("DOWN")
		self.assertEqual(repr(d), "Direction('DOWN')")
	def test_Direction_7(self):
		d = Direction("LEFT")
		self.assertEqual(repr(d), "Direction('LEFT')")
		d = Direction("RIGHT")
		self.assertEqual(repr(d), "Direction('RIGHT')")
	
	def test_Direction_8(self):
		d1 = Direction("DOWN")
		d2 = Direction("UP")
		self.assertNotEqual(d1,d2)
	
	def test_Direction_9(self):
		d1 = Direction("DOWN")
		d2 = Direction("DOWN")
		self.assertEqual(d1,d2)
	
	
		
	#---------------------------------------------------------------------
	
	# class TileError
	
	def test_TileError_1(self):
		try:
			d = Direction("not a valid direction string")
		except TileError as e:
			return
		raise ValueError("your Direction() constructor should only allow the four direction strings UP, DOWN, LEFT, and RIGHT")
	
	def test_TileError_2(self):
		e = TileError("can't move LEFT.")
		self.assertTrue(isinstance(e,Exception))
		self.assertEqual(e.msg.lower(), "can't move left.")
	
	def test_TileError_3(self):
		e = TileError("can't move RIGHT.")
		self.assertTrue(isinstance(e,Exception))
		self.assertEqual(str(e).lower(), "can't move right.")
	
	def test_TileError_4(self):
		e = TileError("can't move DOWN.")
		self.assertTrue(isinstance(e,Exception))
		self.assertEqual(repr(e).lower(), "TileError('''can't move down.''')".lower())
	
	#---------------------------------------------------------------------
	
	# class Puzzle
	
	def test_Puzzle_1(self):
		p = Puzzle()
		self.assertEqual(p.grid[2][1].value, 10)
		self.assertEqual(p.grid[3][3].value, None)
	
	def test_Puzzle_2(self):
		p = Puzzle()
		self.assertEqual(str(p), " 1  2  3  4\n 5  6  7  8\n 9 10 11 12\n13 14 15 <>\n")	
	
	def test_Puzzle_3(self):
		p = Puzzle()
		self.assertEqual(repr(p), 'Puzzle([[Tile(1), Tile(2), Tile(3), Tile(4)], [Tile(5), Tile(6), Tile(7), Tile(8)], [Tile(9), Tile(10), Tile(11), Tile(12)], [Tile(13), Tile(14), Tile(15), Tile(None)]])')	
	
	
	def test_display_1(self):
		# make the puzzle
		p = Puzzle()
		
		# temporarily change printing to target 
		import sys
		sys.stdout = open("temptestingfile.txt",'w')
		p.display()
		sys.stdout.close()
		sys.stdout = sys.__stdout__
		
		# read what got printed
		with open("temptestingfile.txt") as f:
			s = f.read()
		import os
		if os.path.exists("temptestingfile.txt"):
			os.remove("temptestingfile.txt")
		# we expect this string...
		stringversion = " 1  2  3  4\n 5  6  7  8\n 9 10 11 12\n13 14 15 <>\n"
		# ignoring whitespace on the edges (via .strip()), do they match?
		self.assertEquals(s.strip(),stringversion.strip())
		
	def test_find_opening_1(self):
		p = Puzzle()
		self.assertEqual(p.find_opening(),(3,3))
	
	def test_find_opening_2(self):
		p = Puzzle()
		# move some pieces around...
		swaptiles(p,(3,3),(1,2))
		# check that we find the new opening.
		self.assertEqual(p.find_opening(),(1,2))
	
	def test_find_opening_3(self):
		p = Puzzle()
		# move some pieces around...
		swaptiles(p,(0,0),(3,3))
		
		# check that we find the new opening.
		self.assertEqual(p.find_opening(),(0,0))
	
	def test_find_opening_4(self):
		p = Puzzle()
		p.grid[3][3] = Tile(12)
		# check that we find the new opening.
		try:
			pair = p.find_opening()
		except TileError as e:
			self.assertEqual(e.msg.lower(), "no blank spot found".lower())
	
	def test_move_1(self):
		p = Puzzle()
		swaptiles(p,(1,1),(3,3))
		p.move(UP)
		self.assertEqual(p.grid[1][1].value,10)
		self.assertEqual(puzzvals(p),[1,2,3,4,5,10,7,8,9,None,11,12,13,14,15,6])
	
	def test_move_2(self):
		p = Puzzle()
		swaptiles(p,(1,1),(3,3))
		p.move(DOWN)
		self.assertEqual(p.grid[1][1].value,2)
		self.assertEqual(puzzvals(p),[1,None,3,4,5,2,7,8,9,10,11,12,13,14,15,6])
	
	def test_move_3(self):
		p = Puzzle()
		swaptiles(p,(1,1),(3,3))
		p.move(RIGHT)
		self.assertEqual(p.grid[1][1].value,5)
		self.assertEqual(puzzvals(p),[1,2,3,4,None,5,7,8,9,10,11,12,13,14,15,6])
	
	def test_move_4(self):
		p = Puzzle()
		swaptiles(p,(1,1),(3,3))
		p.move(LEFT)
		self.assertEqual(p.grid[1][1].value,7)
		self.assertEqual(puzzvals(p),[1,2,3,4,5,7,None,8,9,10,11,12,13,14,15,6])
	
	
	def test_move_5(self):
		p = Puzzle()
		swaptiles(p,(0,0),(3,3))
		try:
			p.move(DOWN)
		except TileError as e:
			self.assertEqual(e.msg.lower(), "can't move down")
	
	def test_move_6(self):
		p = Puzzle()
		swaptiles(p,(0,0),(3,3))
		try:
			p.move(RIGHT)
		except TileError as e:
			self.assertEqual(e.msg.lower(), "can't move right")
	
	def test_move_7(self):
		p = Puzzle()
		try:
			p.move(LEFT)
		except TileError as e:
			self.assertEqual(e.msg.lower(), "can't move left")
	
	def test_move_8(self):
		p = Puzzle()
		try:
			p.move(UP)
		except TileError as e:
			self.assertEqual(e.msg.lower(), "can't move up")
	
	def test_is_solved_1(self):
		p = Puzzle()
		# if your puzzles start solved, is_sovled reports True.
		self.assertEqual(p.is_solved(), puzzvals(p)==[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None])
	
	def test_is_solved_2(self):
		p = Puzzle()
		# and really, you should be starting solved as directed.
		self.assertTrue(p.is_solved())
	
	def test_is_solved_3(self):
		p = Puzzle()
		swaptiles(p,(1,2),(3,3))
		
		# because we've moved a piece or two, it is not solved.
		self.assertFalse(p.is_solved())
	
	def test_is_solved_4(self):
		p = Puzzle()
		swaptiles(p,(1,2),(3,3))
		swaptiles(p,(2,3),(1,3))
		swaptiles(p,(3,0),(0,0))
		
		self.assertEqual(puzzvals(p), [13,2,3,4,5,6,None,12,9,10,11,8,1,14,15,7])
		# because we've moved a piece or two, it is not solved.
		self.assertFalse(p.is_solved())
	
	def test_is_solved_5(self):
		p = Puzzle()
		try:
			p.move(UP)
		except TileError as e:
			pass
		#  because the move wasn't possible, and we recovered, no change
		# should have occurred and our solved puzzle is still solved.
		self.assertTrue(p.is_solved())
	
	def test_scramble_1(self):
		p = Puzzle()
		p.scramble(0)
		self.assertEqual(puzzvals(p), [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None])
	
	def test_scramble_2(self):
		import random
		random.seed(1)
		p = Puzzle()
		# with seed==1, the single attempted move happens to be DOWN
		p.scramble(1)
		self.assertEqual(puzzvals(p), [1,2,3,4,5,6,7,8,9,10,11,None,13,14,15,12])
		
	def test_scramble_3(self):
		import random
		random.seed(1)
		p = Puzzle()
		# with seed==1, the attempted moves are:
		# DOWN UP LEFT UP RIGHT RIGHT RIGHT RIGHT DOWN UP
		p.scramble(10)
		self.assertEqual(puzzvals(p), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, 13, 14, 15])
	
	def test_scramble_4(self):
		import random
		random.seed("we visited Pluto on July 14th, 2015!")
		p = Puzzle()
		p.scramble(1000)
		self.assertEqual(puzzvals(p), [12, 4, None, 6, 11, 8, 5, 13, 2, 9, 14, 15, 7, 1, 10, 3])
		
	#---------------------------------------------------------------------
	
	# extra credit - arbitrary grid sizes!
	
	def test_extra_credit_1(self):
		p = Puzzle(width=3, height=3)
		self.assertEqual(puzzvals(p),[1,2,3,4,5,6,7,8,None])
	
	def test_extra_credit_2(self):
		p = Puzzle(height=5, width=2)
		self.assertEqual(puzzvals(p),[1,2,3,4,5,6,7,8,9,None])
		manualgrid = [	[Tile(1),Tile(2)],
						[Tile(3),Tile(4)],
						[Tile(5),Tile(6)],
						[Tile(7),Tile(8)],
						[Tile(9),Tile(None)]
					 ]
		# make sure the same value tile is at each spot, and that they have
		# the same dimensions.
		for i in range(len(manualgrid)):
			for j in range(len(manualgrid[i])):
				self.assertEqual(p.grid[i][j].value,manualgrid[i][j].value)
	
	def test_extra_credit_3(self):
		p = Puzzle(height=3, width=6)
		self.assertEqual(puzzvals(p),[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,None])
		manualgrid = [	[Tile(1) ,Tile(2), Tile(3), Tile(4), Tile(5), Tile(6)],
						[Tile(7) ,Tile(8), Tile(9), Tile(10),Tile(11),Tile(12)],
						[Tile(13),Tile(14),Tile(15),Tile(16),Tile(17),Tile(None)]
					 ]
		# make sure the same value tile is at each spot, and that they have
		# the same dimensions.
		for i in range(len(manualgrid)):
			for j in range(len(manualgrid[i])):
				self.assertEqual(p.grid[i][j].value,manualgrid[i][j].value)
	
	def test_extra_credit_4(self):
		self.maxDiff = None
		p = Puzzle(height=2, width=2)
		self.assertEqual(puzzvals(p),[1,2,3,None])
	
	def test_extra_credit_5(self):
		self.maxDiff = None
		p = Puzzle(height=15, width=20)
		import random
		random.seed("extra credits, yay!")
		p.scramble(100000)
		answer = [104, 173, 241, 184, 181, 266, 262, 112, 67, 159, 125, 149, 93, 274, 98, 188, 196, 229, 202, 65, 42, 168, 16, 206, 264, 95, 201, 97, 48, 223, 180, 75, 6, 150, 70, 32, 30, 297, 172, 13, 27, 23, 226, 121, 43, 127, 52, 116, 193, 2, 118, 8, 187, 200, 37, 33, 212, 60, 108, 38, 282, 271, 253, 63, 122, 269, 110, 178, 139, 111, 1, 124, 89, 222, 59, 171, 199, 50, 114, 66, 25, 83, 170, 87, 91, 275, 144, 147, 69, 47, 299, 252, 151, 140, 294, 153, 250, 239, 279, 174, 105, 34, 145, 88, 160, 120, 40, 84, 209, 156, 291, 53, 211, 237, 197, 11, 19, 138, 251, 35, 76, 213, None, 4, 113, 109, 240, 248, 143, 221, 106, 51, 215, 119, 142, 278, 208, 175, 18, 15, 152, 68, 103, 85, 183, 26, 115, 210, 163, 56, 100, 295, 74, 134, 31, 7, 236, 256, 57, 189, 286, 191, 129, 3, 101, 290, 130, 54, 263, 39, 192, 62, 276, 164, 232, 247, 231, 117, 94, 268, 141, 146, 102, 148, 46, 293, 99, 9, 265, 44, 169, 14, 79, 235, 29, 166, 58, 12, 123, 289, 249, 10, 284, 230, 261, 288, 233, 185, 298, 217, 5, 92, 128, 204, 280, 182, 218, 220, 96, 194, 245, 137, 203, 224, 285, 41, 45, 155, 82, 259, 238, 61, 28, 246, 272, 135, 158, 214, 216, 80, 190, 49, 165, 161, 81, 244, 283, 198, 186, 219, 242, 20, 71, 255, 258, 177, 260, 36, 277, 132, 176, 64, 24, 267, 86, 136, 205, 107, 225, 73, 17, 227, 90, 254, 131, 273, 234, 179, 287, 157, 21, 22, 243, 55, 207, 281, 162, 228, 270, 126, 133, 195, 77, 257, 167, 296, 72, 292, 78, 154]
		self.assertEqual(puzzvals(p),answer)

	
# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		# find all methods that begin with "test".
		fs = []
		want_all = wants==None
		
		for func in AllTests.__dict__:
			# append regular tests
			# drop any digits from the end of str(func).
			dropnum = str(func)
			while dropnum[-1] in "1234567890":
				dropnum = dropnum[:-1]
			
			if func in ['__doc__', '__module__']:
				continue
			# check if we want this one.
			want_this_one = want_all
			if wants != None:
				for w in wants:
					is_ec = dropnum==("test_extra_credit_"+w+"_")
					if is_ec:
						want_this_one = False
						break
					is_test = dropnum==("test_"+w+"_")
					check = is_test and ((not is_ec) or (is_ec and (not BATCH_MODE)))
					want_this_one = want_this_one or check
			
			if want_this_one:
				fs.append(AllTests(str(func)))
		
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self,wants):
			# find all methods that begin with "test".
			fs = []
			want_all = wants==None
			for func in AllTests.__dict__:
				want_this_one = want_all
				if wants != None:
					for w in wants:
						is_ec = (str(func).startswith("test_extra_credit_"+w))
						want_this_one = want_this_one or is_ec
				
				if BATCH_MODE and want_this_one:
					fs.append(AllTests(str(func)))
			
			# call parent class's constructor.
			unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
	info = os.walk(dir)
	filenames = []
	for (dirpath,dirnames,filez) in info:
#		print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			filenames.append(os.path.join(dirpath,file))
#		print(dirpath,dirnames,filez,"\n")
#		filenames.extend(os.path.join(dirpath, filez))
	return filenames

def main():
	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\"python3 tester4L.py gmason76_2xx_L4.py\"")
	want_all = len(sys.argv) <=2
	wants = []
	
	# remove batch_mode signifiers from want-candidates.
	want_candidates = sys.argv[2:]
	for i in range(len(want_candidates)-1,-1,-1):
		if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
			del want_candidates[i]
	
	if not want_all:
		print("args: ",sys.argv)
		for w in want_candidates:
			if w in REQUIRED_DEFNS:
				wants.append(w)
			elif w in SUB_DEFNS:
				wants.append(w)
			else:
				raise Exception("asked to limit testing to unknown function '%s'."%w)
	else:
		wants = None # signifies that we want them all.
	
	if not BATCH_MODE:
		run_file(sys.argv[1],wants)
	else:
		filenames = files_list(sys.argv[1])
	
# 		print(filenames)
	
		results = []
		for filename in filenames:
			try:
				print("\n\n\nRUNNING: "+filename)
				(tag, passed,tried,ec) = run_file(filename,wants)
				results.append((tag,passed,tried,ec))
			except SyntaxError as e:
				results.append((filename+"_SYNTAX_ERROR",0,1))	
			except ValueError as e:
				return (filename+"_VALUE_ERROR",0,1)
			except TypeError as e:
				return (filename+"_TYPE_ERROR",0,1)
			except ImportError as e:
				results.append((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
			except Exception as e:
				return (filename+str(e.__reduce__()[0]),0,1)
			
		print("\n\n\nGRAND RESULTS:\n")
		for (tag, passed, tried, ec) in results:
			print(("%.0f%%  (%d/%d, %dEC) - " % (passed/tried*100 + ec, passed, tried, ec))+tag)

# this will group all the tests together, prepare them as 
# a test suite, and run them.
def run_file(filename,wants=[]):
	
	# move the student's code to a valid file.
	shutil.copyfile(filename,"student.py")
	# wait half a second for file I/O to catch up...
		
	# import student's code, and *only* copy over the expected functions
	# for later use.
	import imp
	count = 0
	while True:
		try:
			import student
			imp.reload(student)
			break
		except ImportError as e:
			print("import error getting student.. trying again. "+os.getcwd(), os.path.exists("student.py"))
			time.sleep(0.5)
			count+=1
			if count>3:
				raise ImportError("too many attempts at importing!")
		except SyntaxError as e:
			results.append((filename+"_SYNTAX_ERROR",0,1))	
		except ValueError as e:
			return (filename+"_VALUE_ERROR",0,1)
		except TypeError as e:
			return (filename+"_TYPE_ERROR",0,1)
		except ImportError as e:
			results.append((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))	
		except Exception as e:
			return (filename+str(e.__reduce__()[0]),0,1)
		except Exception as e:
			print("didn't get to import student yet... " + e)
	# but we want to re-load this between student runs...
	# the imp module helps us force this reload.s
	
	import student
	imp.reload(student)
	
	# make a global for each expected definition.
	def decoy(name):
		return (lambda x: "<no '%s' definition found>" % name)
		
	for fn in REQUIRED_DEFNS:
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			print("\nNO DEFINITION FOR '%s'." % fn)	
	
	# create an object that can run tests.
	runner1 = unittest.TextTestRunner()
	
	# define the suite of tests that should be run.
	suite1 = TheTestSuite(wants)
	
	# let the runner run the suite of tests.
	ans = runner1.run(suite1)
	num_errors   = len(ans.__dict__['errors'])
	num_failures = len(ans.__dict__['failures'])
	num_tests    = ans.__dict__['testsRun']
	num_passed   = num_tests - num_errors - num_failures
	# print(ans)
	
	
	if BATCH_MODE:
		# do the same for the extra credit.
		runnerEC = unittest.TextTestRunner()
		suiteEC = TheExtraCreditTestSuite(wants)
		ansEC = runnerEC.run(suiteEC)
		num_errorsEC   = len(ansEC.__dict__['errors'])
		num_failuresEC = len(ansEC.__dict__['failures'])
		num_testsEC    = ansEC.__dict__['testsRun']
		num_passedEC   = num_testsEC - num_errorsEC - num_failuresEC
		print(ansEC)
	else:
		num_passedEC = 0
	
	# remove our temporary file.
	os.remove("student.py")
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")
	
	tag = ".".join(filename.split(".")[:-1])
	return (tag, num_passed, num_tests,num_passedEC)

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
	main()
