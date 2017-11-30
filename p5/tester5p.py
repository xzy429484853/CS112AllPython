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
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
# 
# - name all required definitions in REQUIRED_DEFNS. Do not include any unofficial 
#   helper functions. If you want to make helper definitions to use while testing,
#   those can also be added there for clarity.
# 
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
import copy
import importlib

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond 
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.
	
REQUIRED_DEFNS = ["read_file",
				  "add_name",
				  "find_all_years",
				  "new_names",
				  "rank_names_for_one_year",
				  "rank_names",
				  "popularity_by_name",
				  "popularity_by_year",
				  "always_popular_names",
				  "increasing_rank_names",
				  "merge_databases"
				 ]

RENAMED_FILE = "student"


def write_file(filename, contents):
	f = open(filename,'w')
	f.write(contents)
	f.close()

# small csv
file0str = '''"YEAR","GENDER","NAME","COUNT"
"2009","MALE","DANIEL","3423"
"2009","MALE","ANTHONY","3106"
"2009","MALE","ANGEL","3058"
"2009","MALE","JACOB","2978"
"2009","MALE","ALEXANDER","2905"
"2009","MALE","ETHAN","2687"
"2009","MALE","DAVID","2648"
"2009","MALE","ANDREW","2605"
"2009","MALE","MATTHEW","2435"
"2009","MALE","JOSHUA","2435"
"2010","MALE","JACOB","3368"
"2010","MALE","DANIEL","3175"
"2010","MALE","ANTHONY","2882"
"2010","MALE","ALEXANDER","2619"
"2010","MALE","ANGEL","2581"
"2010","MALE","ETHAN","2497"
"2010","MALE","JAYDEN","2460"
"2010","MALE","DAVID","2442"
"2010","MALE","ANDREW","2391"
"2010","MALE","NATHAN","2286"
"2011","MALE","JACOB","3180"
"2011","MALE","DANIEL","2936"
"2011","MALE","JAYDEN","2773"
"2011","MALE","ANTHONY","2716"
"2011","MALE","ALEXANDER","2494"
"2011","MALE","MATTHEW","2490"
"2011","MALE","ETHAN","2408"
"2011","MALE","DAVID","2324"
"2011","MALE","ANDREW","2310"
"2011","MALE","NATHAN","2261"
'''
write_file(".file0.csv",file0str)
ud0 = {('DAVID', 'MALE'): {2009: (2648, None), 2010: (2442, None), 2011: (2324, None)}, ('ANGEL', 'MALE'): {2009: (3058, None), 2010: (2581, None)}, ('DANIEL', 'MALE'): {2009: (3423, None), 2010: (3175, None), 2011: (2936, None)}, ('JACOB', 'MALE'): {2009: (2978, None), 2010: (3368, None), 2011: (3180, None)}, ('ANDREW', 'MALE'): {2009: (2605, None), 2010: (2391, None), 2011: (2310, None)}, ('JAYDEN', 'MALE'): {2010: (2460, None), 2011: (2773, None)}, ('ANTHONY', 'MALE'): {2009: (3106, None), 2010: (2882, None), 2011: (2716, None)}, ('ETHAN', 'MALE'): {2009: (2687, None), 2010: (2497, None), 2011: (2408, None)}, ('JOSHUA', 'MALE'): {2009: (2435, None)}, ('NATHAN', 'MALE'): {2010: (2286, None), 2011: (2261, None)}, ('ALEXANDER', 'MALE'): {2009: (2905, None), 2010: (2619, None), 2011: (2494, None)}, ('MATTHEW', 'MALE'): {2009: (2435, None), 2011: (2490, None)}}
rd0 = {('DAVID', 'MALE'): {2009: (2648, 7), 2010: (2442, 8), 2011: (2324, 8)}, ('ANGEL', 'MALE'): {2009: (3058, 3), 2010: (2581, 5)}, ('JACOB', 'MALE'): {2009: (2978, 4), 2010: (3368, 1), 2011: (3180, 1)}, ('DANIEL', 'MALE'): {2009: (3423, 1), 2010: (3175, 2), 2011: (2936, 2)}, ('JAYDEN', 'MALE'): {2010: (2460, 7), 2011: (2773, 3)}, ('ANTHONY', 'MALE'): {2009: (3106, 2), 2010: (2882, 3), 2011: (2716, 4)}, ('ETHAN', 'MALE'): {2009: (2687, 6), 2010: (2497, 6), 2011: (2408, 7)}, ('JOSHUA', 'MALE'): {2009: (2435, 9)}, ('NATHAN', 'MALE'): {2010: (2286, 10), 2011: (2261, 10)}, ('ANDREW', 'MALE'): {2009: (2605, 8), 2010: (2391, 9), 2011: (2310, 9)}, ('MATTHEW', 'MALE'): {2009: (2435, 9), 2011: (2490, 6)}, ('ALEXANDER', 'MALE'): {2009: (2905, 5), 2010: (2619, 4), 2011: (2494, 5)}}

# good for read_file; there are commas in someone's name field
file1str = '''"YEAR","GENDER","NAME","COUNT"
"20","MALE","DOUG, JR","10"
"20","MALE","QUINCY, III","8"
"20","MALE","ALI","20"
"20","MALE","BHARAT","17"
"20","MALE","CHAD","6"
"20","MALE","DAVID","24"
"20","MALE","EGGBERT","2"
'''
write_file(".file1.csv",file1str)
ud1 = {('EGGBERT', 'MALE'): {20: (2, None)}, ('DOUG, JR', 'MALE'): {20: (10, None)}, ('ALI', 'MALE'): {20: (20, None)}, ('DAVID', 'MALE'): {20: (24, None)}, ('CHAD', 'MALE'): {20: (6, None)}, ('QUINCY, III', 'MALE'): {20: (8, None)}, ('BHARAT', 'MALE'): {20: (17, None)}}
rd1 = {('EGGBERT', 'MALE'): {20: (2, 7)}, ('DOUG, JR', 'MALE'): {20: (10, 4)}, ('ALI', 'MALE'): {20: (20, 2)}, ('DAVID', 'MALE'): {20: (24, 1)}, ('CHAD', 'MALE'): {20: (6, 6)}, ('QUINCY, III', 'MALE'): {20: (8, 5)}, ('BHARAT', 'MALE'): {20: (17, 3)}}

# same name occurs in different years (DANIEL)
# a name exists in just one year (ZUUL, HIGHLANDER)
# all male
file2str = '''"YEAR","GENDER","NAME","COUNT"
"2009","MALE","DANIEL","400"
"2010","MALE","DANIEL","425"
"2011","MALE","DANIEL","450"
"2012","MALE","DANIEL","475"
"2011","MALE","BART","300"
"2011","MALE","CHASE","350"
"2012","MALE","BART","400"
"2012","MALE","CHASE","325"
"2011","MALE","ZUUL","2"
"2011","MALE","HIGHLANDER","1"
'''
write_file(".file2.csv",file2str)
ud2 = {('DANIEL',     'MALE'): {2009: (400, None), 2010: (425, None), 2011: (450, None), 2012: (475, None)},
	   ('BART',       'MALE'):                                       {2011: (300, None), 2012: (400, None)},
	   ('HIGHLANDER', 'MALE'):                                       {2011: (  1, None)},
	   ('ZUUL',       'MALE'):                                       {2011: (  2, None)},
	   ('CHASE',      'MALE'):                                       {2011: (350, None), 2012: (325, None)}
	  }
rd2 = {('DANIEL',     'MALE'): {2009: (400, 1), 2010: (425, 1), 2011: (450, 1), 2012: (475, 1)},
	   ('BART',       'MALE'):                                 {2011: (300, 3), 2012: (400, 2)},
	   ('CHASE',      'MALE'):                                 {2011: (350, 2), 2012: (325, 3)},
	   ('HIGHLANDER', 'MALE'):                                 {2011: (1, 5)},
	   ('ZUUL',       'MALE'):                                 {2011: (2, 4)}
	   }


#	def test_increasing_rank_names_2 (self): self.assertEqual(increasing_rank_names(rd2,"MALE",2011,2012),['BART'])
#	def test_increasing_rank_names_3 (self): self.assertEqual(increasing_rank_names(rd3,"FEMALE",2011,2012),['BEA'])

# all names are in all present years.
# all female
file3str = '''"YEAR","GENDER","NAME","COUNT"
"2010","FEMALE","AMY","500"
"2010","FEMALE","BEA","400"
"2010","FEMALE","CAT","300"
"2011","FEMALE","AMY","400"
"2011","FEMALE","BEA","500"
"2011","FEMALE","CAT","200"
"2012","FEMALE","AMY","500"
"2012","FEMALE","BEA","400"
"2012","FEMALE","CAT","200"
'''
write_file(".file3.csv",file3str)
ud3 = {('AMY', 'FEMALE'): {2010: (500, None), 2011: (400, None), 2012: (500, None)}, ('BEA', 'FEMALE'): {2010: (400, None), 2011: (500, None), 2012: (400, None)}, ('CAT', 'FEMALE'): {2010: (300, None), 2011: (200, None), 2012: (200, None)}}
rd3 = {('AMY', 'FEMALE'): {2010: (500, 1), 2011: (400, 2), 2012: (500, 1)},
       ('BEA', 'FEMALE'): {2010: (400, 2), 2011: (500, 1), 2012: (400, 2)},
       ('CAT', 'FEMALE'): {2010: (300, 3), 2011: (200, 3), 2012: (200, 3)}}

# names appear and disappear in different years.
# names first show up in different years.
file4str = '''"YEAR","GENDER","NAME","COUNT"
"2011","MALE","ALI","200"
"2012","MALE","ALI","200"
"2013","MALE","ALI","200"
"2014","MALE","ALI","200"
"2015","MALE","ALI","200"
"2012","MALE","BOB","200"
"2013","MALE","BOB","200"
"2014","MALE","BOB","200"
"2013","MALE","LUKE","200"
"2015","MALE","LUKE","200"
"2014","MALE","JEFF","200"
'''
write_file(".file4.csv",file4str)
ud4 = {('LUKE', 'MALE'): {2013: (200, None), 2015: (200, None)}, ('JEFF', 'MALE'): {2014: (200, None)}, ('BOB', 'MALE'): {2012: (200, None), 2013: (200, None), 2014: (200, None)}, ('ALI', 'MALE'): {2011: (200, None), 2012: (200, None), 2013: (200, None), 2014: (200, None), 2015: (200, None)}}
rd4 = {('LUKE', 'MALE'): {2013: (200, 1), 2015: (200, 1)}, ('JEFF', 'MALE'): {2014: (200, 1)}, ('BOB', 'MALE'): {2012: (200, 1), 2013: (200, 1), 2014: (200, 1)}, ('ALI', 'MALE'): {2011: (200, 1), 2012: (200, 1), 2013: (200, 1), 2014: (200, 1), 2015: (200, 1)}}

# more than ten names in a year
# no ties between counts
file5str = '''"YEAR","GENDER","NAME","COUNT"
"2015","FEMALE","A","20"
"2015","FEMALE","B","19"
"2015","FEMALE","C","18"
"2015","FEMALE","D","17"
"2015","FEMALE","E","16"
"2015","FEMALE","F","15"
"2015","FEMALE","G","14"
"2015","FEMALE","H","13"
"2015","FEMALE","I","12"
"2015","FEMALE","J","11"
"2015","FEMALE","K","10"
"2015","FEMALE","L","9"
"2015","FEMALE","M","8"
"2015","FEMALE","N","7"
"2015","FEMALE","O","6"
"2015","FEMALE","P","5"
"2015","FEMALE","Q","4"
"2015","FEMALE","R","3"
"2015","FEMALE","S","2"
"2015","FEMALE","T","1"
'''
write_file(".file5.csv",file5str)
ud5 = {('C', 'FEMALE'): {2015: (18, None)}, ('N', 'FEMALE'): {2015: (7, None)}, ('A', 'FEMALE'): {2015: (20, None)}, ('S', 'FEMALE'): {2015: (2, None)}, ('J', 'FEMALE'): {2015: (11, None)}, ('I', 'FEMALE'): {2015: (12, None)}, ('B', 'FEMALE'): {2015: (19, None)}, ('G', 'FEMALE'): {2015: (14, None)}, ('T', 'FEMALE'): {2015: (1, None)}, ('K', 'FEMALE'): {2015: (10, None)}, ('Q', 'FEMALE'): {2015: (4, None)}, ('M', 'FEMALE'): {2015: (8, None)}, ('O', 'FEMALE'): {2015: (6, None)}, ('E', 'FEMALE'): {2015: (16, None)}, ('D', 'FEMALE'): {2015: (17, None)}, ('R', 'FEMALE'): {2015: (3, None)}, ('F', 'FEMALE'): {2015: (15, None)}, ('P', 'FEMALE'): {2015: (5, None)}, ('H', 'FEMALE'): {2015: (13, None)}, ('L', 'FEMALE'): {2015: (9, None)}}
rd5 = {('C', 'FEMALE'): {2015: (18, 3)}, ('N', 'FEMALE'): {2015: (7, 14)}, ('A', 'FEMALE'): {2015: (20, 1)}, ('J', 'FEMALE'): {2015: (11, 10)}, ('I', 'FEMALE'): {2015: (12, 9)}, ('B', 'FEMALE'): {2015: (19, 2)}, ('G', 'FEMALE'): {2015: (14, 7)}, ('K', 'FEMALE'): {2015: (10, 11)}, ('R', 'FEMALE'): {2015: (3, 18)}, ('M', 'FEMALE'): {2015: (8, 13)}, ('H', 'FEMALE'): {2015: (13, 8)}, ('O', 'FEMALE'): {2015: (6, 15)}, ('E', 'FEMALE'): {2015: (16, 5)}, ('T', 'FEMALE'): {2015: (1, 20)}, ('S', 'FEMALE'): {2015: (2, 19)}, ('F', 'FEMALE'): {2015: (15, 6)}, ('P', 'FEMALE'): {2015: (5, 16)}, ('D', 'FEMALE'): {2015: (17, 4)}, ('Q', 'FEMALE'): {2015: (4, 17)}, ('L', 'FEMALE'): {2015: (9, 12)}}

# tie for first in a year (2012)
# names that increase and decrease over different years
file6str = '''"YEAR","GENDER","NAME","COUNT"
"2010","MALE","S","10"
"2011","MALE","S","10"
"2012","MALE","S","10"
"2013","MALE","S","10"
"2010","MALE","T","8"
"2011","MALE","T","9"
"2012","MALE","T","10"
"2013","MALE","T","11"
"2010","MALE","U","15"
"2011","MALE","U","10"
"2012","MALE","U","5"
"2013","MALE","U","1"
"2012","MALE","V","10"
"2012","MALE","W","10"
"2012","MALE","X","10"
"2012","MALE","Y","10"
"2013","MALE","V","5"
"2013","MALE","W","4"
"2013","MALE","X","13"
"2013","MALE","Y","10"
'''
write_file(".file6.csv",file6str)
ud6 = {('X', 'MALE'): {2012: (10, None), 2013: (13, None)}, ('V', 'MALE'): {2012: (10, None), 2013: (5, None)}, ('Y', 'MALE'): {2012: (10, None), 2013: (10, None)}, ('W', 'MALE'): {2012: (10, None), 2013: (4, None)}, ('T', 'MALE'): {2010: (8, None), 2011: (9, None), 2012: (10, None), 2013: (11, None)}, ('U', 'MALE'): {2010: (15, None), 2011: (10, None), 2012: (5, None), 2013: (1, None)}, ('S', 'MALE'): {2010: (10, None), 2011: (10, None), 2012: (10, None), 2013: (10, None)}}
rd6 = {('X', 'MALE'): {2012: (10, 1), 2013: (13, 1)}, ('V', 'MALE'): {2012: (10, 1), 2013: (5, 5)}, ('Y', 'MALE'): {2012: (10, 1), 2013: (10, 3)}, ('W', 'MALE'): {2012: (10, 1), 2013: (4, 6)}, ('U', 'MALE'): {2010: (15, 1), 2011: (10, 1), 2012: (5, 7), 2013: (1, 7)}, ('T', 'MALE'): {2010: (8, 3), 2011: (9, 3), 2012: (10, 1), 2013: (11, 2)}, ('S', 'MALE'): {2010: (10, 2), 2011: (10, 1), 2012: (10, 1), 2013: (10, 3)}}

# tie for second, in 2012
# highest count in one year, but we can seek rankings in another year
file7str = '''"YEAR","GENDER","NAME","COUNT"
"2011","FEMALE","A","100"
"2012","FEMALE","A","50"
"2012","FEMALE","B","10"
"2012","FEMALE","C","10"
"2012","FEMALE","D","5"
"2013","FEMALE","A","1000"
'''
write_file(".file7.csv",file7str)
ud7 = {('B', 'FEMALE'): {2012: (10, None)}, ('C', 'FEMALE'): {2012: (10, None)}, ('A', 'FEMALE'): {2011: (100, None), 2012: (50, None), 2013: (1000, None)}, ('D', 'FEMALE'): {2012: (5, None)}}
rd7 = {('B', 'FEMALE'): {2012: (10, 2)}, ('C', 'FEMALE'): {2012: (10, 2)}, ('A', 'FEMALE'): {2011: (100, 1), 2012: (50, 1), 2013: (1000, 1)}, ('D', 'FEMALE'): {2012: (5, 4)}}

# tie for 4th
# names arrive in different years
file8str = '''"YEAR","GENDER","NAME","COUNT"
"2008","MALE","B","90"
"2009","MALE","B","90"
"2009","MALE","C","90"
"2010","MALE","A","90"
"2010","MALE","B","90"
"2010","MALE","C","90"
"2011","MALE","A","90"
"2011","MALE","B","80"
"2011","MALE","C","70"
"2011","MALE","D","60"
"2011","MALE","E","60"
"2011","MALE","F","1"
'''
write_file(".file8.csv",file8str)
ud8 = {('B', 'MALE'): {2008: (90, None), 2009: (90, None), 2010: (90, None), 2011: (80, None)}, ('F', 'MALE'): {2011: (1, None)}, ('C', 'MALE'): {2009: (90, None), 2010: (90, None), 2011: (70, None)}, ('E', 'MALE'): {2011: (60, None)}, ('D', 'MALE'): {2011: (60, None)}, ('A', 'MALE'): {2010: (90, None), 2011: (90, None)}}
rd8 = {('B', 'MALE'): {2008: (90, 1), 2009: (90, 1), 2010: (90, 1), 2011: (80, 2)}, ('C', 'MALE'): {2009: (90, 1), 2010: (90, 1), 2011: (70, 3)}, ('E', 'MALE'): {2011: (60, 4)}, ('D', 'MALE'): {2011: (60, 4)}, ('F', 'MALE'): {2011: (1, 6)}, ('A', 'MALE'): {2010: (90, 1), 2011: (90, 1)}}

# just one year
# both genders
file9str = '''"YEAR","GENDER","NAME","COUNT"
"2000","MALE","A","26"
"2000","MALE","B","25"
"2000","MALE","C","24"
"2000","MALE","D","23"
"2000","MALE","E","22"
"2000","MALE","F","21"
"2000","MALE","G","20"
"2000","MALE","H","19"
"2000","MALE","I","18"
"2000","MALE","J","17"
"2000","MALE","K","16"
"2000","MALE","L","15"
"2000","FEMALE","M","14"
"2000","FEMALE","N","13"
"2000","FEMALE","O","12"
"2000","FEMALE","P","11"
"2000","FEMALE","Q","10"
"2000","FEMALE","R","9"
"2000","FEMALE","S","8"
"2000","FEMALE","T","7"
"2000","FEMALE","U","6"
"2000","FEMALE","V","5"
"2000","FEMALE","W","4"
"2000","FEMALE","X","3"
'''
write_file(".file9.csv",file9str)
ud9 = {('N', 'FEMALE'): {2000: (13, None)}, ('H', 'MALE'): {2000: (19, None)}, ('J', 'MALE'): {2000: (17, None)}, ('T', 'FEMALE'): {2000: (7, None)}, ('E', 'MALE'): {2000: (22, None)}, ('D', 'MALE'): {2000: (23, None)}, ('A', 'MALE'): {2000: (26, None)}, ('M', 'FEMALE'): {2000: (14, None)}, ('V', 'FEMALE'): {2000: (5, None)}, ('S', 'FEMALE'): {2000: (8, None)}, ('U', 'FEMALE'): {2000: (6, None)}, ('K', 'MALE'): {2000: (16, None)}, ('G', 'MALE'): {2000: (20, None)}, ('F', 'MALE'): {2000: (21, None)}, ('L', 'MALE'): {2000: (15, None)}, ('X', 'FEMALE'): {2000: (3, None)}, ('R', 'FEMALE'): {2000: (9, None)}, ('W', 'FEMALE'): {2000: (4, None)}, ('I', 'MALE'): {2000: (18, None)}, ('B', 'MALE'): {2000: (25, None)}, ('O', 'FEMALE'): {2000: (12, None)}, ('C', 'MALE'): {2000: (24, None)}, ('P', 'FEMALE'): {2000: (11, None)}, ('Q', 'FEMALE'): {2000: (10, None)}}
rd9 = {('U', 'FEMALE'): {2000: (6, 9)}, ('N', 'FEMALE'): {2000: (13, 2)}, ('H', 'MALE'): {2000: (19, 8)}, ('D', 'MALE'): {2000: (23, 4)}, ('S', 'FEMALE'): {2000: (8, 7)}, ('T', 'FEMALE'): {2000: (7, 8)}, ('E', 'MALE'): {2000: (22, 5)}, ('J', 'MALE'): {2000: (17, 10)}, ('A', 'MALE'): {2000: (26, 1)}, ('M', 'FEMALE'): {2000: (14, 1)}, ('K', 'MALE'): {2000: (16, 11)}, ('V', 'FEMALE'): {2000: (5, 10)}, ('G', 'MALE'): {2000: (20, 7)}, ('F', 'MALE'): {2000: (21, 6)}, ('Q', 'FEMALE'): {2000: (10, 5)}, ('X', 'FEMALE'): {2000: (3, 12)}, ('R', 'FEMALE'): {2000: (9, 6)}, ('W', 'FEMALE'): {2000: (4, 11)}, ('I', 'MALE'): {2000: (18, 9)}, ('B', 'MALE'): {2000: (25, 2)}, ('O', 'FEMALE'): {2000: (12, 3)}, ('C', 'MALE'): {2000: (24, 3)}, ('P', 'FEMALE'): {2000: (11, 4)}, ('L', 'MALE'): {2000: (15, 12)}}

# lots of trading rankings.
file10str = '''"YEAR","GENDER","NAME","COUNT"
"2000","FEMALE","A","100"
"2000","FEMALE","B","90"
"2000","FEMALE","C","30"
"2000","FEMALE","D","20"
"2000","FEMALE","E","70"
"2000","FEMALE","F","40"
"2001","FEMALE","A","80"
"2001","FEMALE","B","10"
"2001","FEMALE","C","100"
"2001","FEMALE","D","30"
"2001","FEMALE","E","90"
"2001","FEMALE","F","40"
"2002","FEMALE","A","100"
"2002","FEMALE","B","80"
"2002","FEMALE","C","90"
"2002","FEMALE","D","60"
"2002","FEMALE","E","20"
"2002","FEMALE","F","70"
"2003","FEMALE","A","90"
"2003","FEMALE","B","100"
"2003","FEMALE","C","20"
"2003","FEMALE","D","80"
"2003","FEMALE","E","10"
"2003","FEMALE","F","50"
'''
write_file(".file10.csv",file10str)
ud10 = {('C', 'FEMALE'): {2000: (30, None), 2001: (100, None), 2002: (90, None), 2003: (20, None)}, ('F', 'FEMALE'): {2000: (40, None), 2001: (40, None), 2002: (70, None), 2003: (50, None)}, ('A', 'FEMALE'): {2000: (100, None), 2001: (80, None), 2002: (100, None), 2003: (90, None)}, ('E', 'FEMALE'): {2000: (70, None), 2001: (90, None), 2002: (20, None), 2003: (10, None)}, ('D', 'FEMALE'): {2000: (20, None), 2001: (30, None), 2002: (60, None), 2003: (80, None)}, ('B', 'FEMALE'): {2000: (90, None), 2001: (10, None), 2002: (80, None), 2003: (100, None)}}
rd10 = {('B', 'FEMALE'): {2000: (90, 2), 2001: (10, 6), 2002: (80, 3), 2003: (100, 1)}, ('C', 'FEMALE'): {2000: (30, 5), 2001: (100, 1), 2002: (90, 2), 2003: (20, 5)}, ('A', 'FEMALE'): {2000: (100, 1), 2001: (80, 3), 2002: (100, 1), 2003: (90, 2)}, ('E', 'FEMALE'): {2000: (70, 3), 2001: (90, 2), 2002: (20, 6), 2003: (10, 6)}, ('D', 'FEMALE'): {2000: (20, 6), 2001: (30, 5), 2002: (60, 5), 2003: (80, 3)}, ('F', 'FEMALE'): {2000: (40, 4), 2001: (40, 4), 2002: (70, 4), 2003: (50, 4)}}

# END SPECIALIZATION SECTION
############################################################################
############################################################################

# enter batch mode by giving a directory to work on.
BATCH_MODE = (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):

	def test_read_file_1 (self): self.assertEqual(read_file(".file0.csv"),ud0)
	def test_read_file_2 (self): self.assertEqual(read_file(".file1.csv"),ud1)
	def test_read_file_3 (self): self.assertEqual(read_file(".file2.csv"),ud2)
	def test_read_file_4 (self): self.assertEqual(read_file(".file3.csv"),ud3)
	def test_read_file_5 (self): self.assertEqual(read_file(".file4.csv"),ud4)
	def test_read_file_6 (self): self.assertEqual(read_file(".file5.csv"),ud5)
	def test_read_file_7 (self): self.assertEqual(read_file(".file6.csv"),ud6)
	def test_read_file_8 (self): self.assertEqual(read_file(".file7.csv"),ud7)
	
	def test_add_name_1 (self):
			"""adding to an empty datbase"""
			d = {}
			add_name(d,"A","MALE",2000,30)
			self.assertEqual(d, {("A","MALE"):{2000:(30,None)}})
	def test_add_name_2 (self):
			"""adding to database where the name is already present"""
			d = {("A","MALE"):{2000:(30,None)}}
			add_name(d,"A","MALE",2001,50)
			self.assertEqual(d, {("A","MALE"):{2000:(30,None),2001:(50,None)}})
	def test_add_name_3 (self):
			"""adding new name to non-empty database"""
			d = {("A","MALE"):{2000:(30,None),2001:(50,None)}}
			add_name(d,"B","FEMALE",2002,2)
			self.assertEqual(d, {("A","MALE"):{2000:(30,None),2001:(50,None)},("B","FEMALE"):{2002:(2,None)}})
	def test_add_name_4 (self):
			"""adding new name (due to gender not matching) in non-empty database."""
			d = {("AVERY","MALE"):{2010:(50,None)}}
			add_name(d,"AVERY","FEMALE",2011,30)
			self.assertEqual(d, {("AVERY","MALE"):{2010:(50,None)},("AVERY","FEMALE"):{2011:(30,None)}})
	def test_add_name_5 (self):
			"""adding earlier year to name in existing database"""
			d = {("A","MALE"):{2000:(30,None),2001:(50,None)}}
			add_name(d,"A","MALE",1999,40)
			self.assertEqual(d, {("A","MALE"):{2000:(30,None),2001:(50,None),1999:(40,None)}})
	def test_add_name_6 (self):
			"""adding to larger database."""
			self.maxDiff = None
			d = copy.deepcopy(ud0)
			add_name(d,"DAVID","MALE",2000,2055)
			self.assertEqual(d, {('DAVID', 'MALE'): {2000:(2055,None), 2009: (2648, None), 2010: (2442, None), 2011: (2324, None)}, ('ANGEL', 'MALE'): {2009: (3058, None), 2010: (2581, None)}, ('DANIEL', 'MALE'): {2009: (3423, None), 2010: (3175, None), 2011: (2936, None)}, ('JACOB', 'MALE'): {2009: (2978, None), 2010: (3368, None), 2011: (3180, None)}, ('ANDREW', 'MALE'): {2009: (2605, None), 2010: (2391, None), 2011: (2310, None)}, ('JAYDEN', 'MALE'): {2010: (2460, None), 2011: (2773, None)}, ('ANTHONY', 'MALE'): {2009: (3106, None), 2010: (2882, None), 2011: (2716, None)}, ('ETHAN', 'MALE'): {2009: (2687, None), 2010: (2497, None), 2011: (2408, None)}, ('JOSHUA', 'MALE'): {2009: (2435, None)}, ('NATHAN', 'MALE'): {2010: (2286, None), 2011: (2261, None)}, ('ALEXANDER', 'MALE'): {2009: (2905, None), 2010: (2619, None), 2011: (2494, None)}, ('MATTHEW', 'MALE'): {2009: (2435, None), 2011: (2490, None)}})
	def test_add_name_7 (self): 
			"""adding new name of unique gender to larger databsae."""
			d = copy.deepcopy(ud5)
			add_name(d,"ANY","MALE",2000,1)
			self.assertEqual(d, {("ANY","MALE"):{2000:(1,None)}, ('C', 'FEMALE'): {2015: (18, None)}, ('N', 'FEMALE'): {2015: (7, None)}, ('A', 'FEMALE'): {2015: (20, None)}, ('S', 'FEMALE'): {2015: (2, None)}, ('J', 'FEMALE'): {2015: (11, None)}, ('I', 'FEMALE'): {2015: (12, None)}, ('B', 'FEMALE'): {2015: (19, None)}, ('G', 'FEMALE'): {2015: (14, None)}, ('T', 'FEMALE'): {2015: (1, None)}, ('K', 'FEMALE'): {2015: (10, None)}, ('Q', 'FEMALE'): {2015: (4, None)}, ('M', 'FEMALE'): {2015: (8, None)}, ('O', 'FEMALE'): {2015: (6, None)}, ('E', 'FEMALE'): {2015: (16, None)}, ('D', 'FEMALE'): {2015: (17, None)}, ('R', 'FEMALE'): {2015: (3, None)}, ('F', 'FEMALE'): {2015: (15, None)}, ('P', 'FEMALE'): {2015: (5, None)}, ('H', 'FEMALE'): {2015: (13, None)}, ('L', 'FEMALE'): {2015: (9, None)}})
	def test_add_name_8 (self): 
			"""adding to existing name for year that others have."""
			d = copy.deepcopy(ud4)
			add_name(d,"BOB","MALE",2015,200)
			self.assertEqual(d, {('LUKE', 'MALE'): {2013: (200, None), 2015: (200, None)}, ('JEFF', 'MALE'): {2014: (200, None)}, ('BOB', 'MALE'): {2012: (200, None), 2013: (200, None), 2014: (200, None), 2015:(200,None)}, ('ALI', 'MALE'): {2011: (200, None), 2012: (200, None), 2013: (200, None), 2014: (200, None), 2015: (200, None)}})
	
	def test_find_all_years_1 (self): self.assertEqual(find_all_years(ud1),[20])
	def test_find_all_years_2 (self): self.assertEqual(find_all_years(ud2),[2009, 2010, 2011, 2012])
	def test_find_all_years_3 (self): self.assertEqual(find_all_years(ud3),[2010, 2011, 2012])
	def test_find_all_years_4 (self): self.assertEqual(find_all_years(ud4),[2011, 2012, 2013, 2014, 2015])
	def test_find_all_years_5 (self): self.assertEqual(find_all_years(ud5),[2015])
	def test_find_all_years_6 (self): self.assertEqual(find_all_years(ud6),[2010, 2011, 2012, 2013])
	def test_find_all_years_7 (self): self.assertEqual(find_all_years(ud7),[2011, 2012, 2013])
	def test_find_all_years_8 (self): self.assertEqual(find_all_years(ud0),[2009, 2010, 2011])
	
	def test_new_names_1 (self): self.assertEqual(new_names(ud4,"MALE",2010, 2013),['ALI','BOB','LUKE'])
	def test_new_names_2 (self): self.assertEqual(new_names(ud4,"MALE",2012, 2015),['LUKE'])
	def test_new_names_3 (self): self.assertEqual(new_names(ud4,"MALE",2013, 2014),['JEFF'])
	def test_new_names_4 (self): self.assertEqual(new_names(ud4,"MALE",2014, 2015),['LUKE'])
	def test_new_names_5 (self): self.assertEqual(new_names(ud8,"MALE",2008, 2011),['A','C','D','E','F'])
	def test_new_names_6 (self): self.assertEqual(new_names(ud8,"MALE",2009, 2011),['A','D','E','F'])
	def test_new_names_7 (self): self.assertEqual(new_names(ud8,"MALE",2010, 2011),['D','E','F'])
	def test_new_names_8 (self): self.assertEqual(new_names(ud8,"MALE",2008, 2010),['A','C'])
	
	def test_rank_names_for_one_year_1 (self):
		"""all same year; no ties."""
		d = copy.deepcopy(ud5)
		rank_names_for_one_year(d,2015)
		self.assertEqual(d,rd5)
	def test_rank_names_for_one_year_2 (self):
		"""multiple years present; no ties in this year."""
		d = copy.deepcopy(ud3)
		rank_names_for_one_year(d,2010)
		self.assertEqual(d,{('CAT', 'FEMALE'): {2010: (300, 3), 2011: (200, None), 2012: (200, None)}, ('AMY', 'FEMALE'): {2010: (500, 1), 2011: (400, None), 2012: (500, None)}, ('BEA', 'FEMALE'): {2010: (400, 2), 2011: (500, None), 2012: (400, None)}})
	def test_rank_names_for_one_year_3 (self):
		"""ties for first."""
		d = copy.deepcopy(ud6)
		rank_names_for_one_year(d,2012)
		self.assertEqual(d,{('W', 'MALE'): {2012: (10, 1), 2013: (4, None)}, ('T', 'MALE'): {2010: (8, None), 2011: (9, None), 2012: (10, 1), 2013: (11, None)}, ('S', 'MALE'): {2010: (10, None), 2011: (10, None), 2012: (10, 1), 2013: (10, None)}, ('Y', 'MALE'): {2012: (10, 1), 2013: (10, None)}, ('U', 'MALE'): {2010: (15, None), 2011: (10, None), 2012: (5, 7), 2013: (1, None)}, ('V', 'MALE'): {2012: (10, 1), 2013: (5, None)}, ('X', 'MALE'): {2012: (10, 1), 2013: (13, None)}})
	def test_rank_names_for_one_year_4 (self):
		"""ties for second."""
		d = copy.deepcopy(ud7)
		rank_names_for_one_year(d,2012)
		self.assertEqual(d,{('A', 'FEMALE'): {2011: (100, None), 2012: (50, 1), 2013: (1000, None)}, ('D', 'FEMALE'): {2012: (5, 4)}, ('B', 'FEMALE'): {2012: (10, 2)}, ('C', 'FEMALE'): {2012: (10, 2)}})
	def test_rank_names_for_one_year_5 (self):
		"""ties for 4th; 6 total names."""
		d = copy.deepcopy(ud8)
		rank_names_for_one_year(d,2011)
		self.assertEqual(d,{('E', 'MALE'): {2011: (60, 4)}, ('F', 'MALE'): {2011: (1, 6)}, ('D', 'MALE'): {2011: (60, 4)}, ('C', 'MALE'): {2009: (90, None), 2010: (90, None), 2011: (70, 3)}, ('B', 'MALE'): {2008: (90, None), 2009: (90, None), 2010: (90, None), 2011: (80, 2)}, ('A', 'MALE'): {2010: (90, None), 2011: (90, 1)}})
	def test_rank_names_for_one_year_6 (self):
		"""make sure it ranks both genders, separately."""
		d = copy.deepcopy(ud9)
		rank_names_for_one_year(d,2000)
		self.assertEqual(d,{('L', 'MALE'): {2000: (15, 12)}, ('E', 'MALE'): {2000: (22, 5)}, ('H', 'MALE'): {2000: (19, 8)}, ('X', 'FEMALE'): {2000: (3, 12)}, ('A', 'MALE'): {2000: (26, 1)}, ('T', 'FEMALE'): {2000: (7, 8)}, ('J', 'MALE'): {2000: (17, 10)}, ('W', 'FEMALE'): {2000: (4, 11)}, ('R', 'FEMALE'): {2000: (9, 6)}, ('G', 'MALE'): {2000: (20, 7)}, ('C', 'MALE'): {2000: (24, 3)}, ('K', 'MALE'): {2000: (16, 11)}, ('I', 'MALE'): {2000: (18, 9)}, ('Q', 'FEMALE'): {2000: (10, 5)}, ('D', 'MALE'): {2000: (23, 4)}, ('B', 'MALE'): {2000: (25, 2)}, ('M', 'FEMALE'): {2000: (14, 1)}, ('N', 'FEMALE'): {2000: (13, 2)}, ('O', 'FEMALE'): {2000: (12, 3)}, ('F', 'MALE'): {2000: (21, 6)}, ('S', 'FEMALE'): {2000: (8, 7)}, ('U', 'FEMALE'): {2000: (6, 9)}, ('V', 'FEMALE'): {2000: (5, 10)}, ('P', 'FEMALE'): {2000: (11, 4)}})
	def test_rank_names_for_one_year_7 (self):
		"""call on two separate years for the same database."""
		d = copy.deepcopy(ud10)
		rank_names_for_one_year(d,2000)
		rank_names_for_one_year(d,2002)
		self.assertEqual(d,{('A', 'FEMALE'): {2000: (100, 1), 2001: (80, None), 2002: (100, 1), 2003: (90, None)}, ('C', 'FEMALE'): {2000: (30, 5), 2001: (100, None), 2002: (90, 2), 2003: (20, None)}, ('B', 'FEMALE'): {2000: (90, 2), 2001: (10, None), 2002: (80, 3), 2003: (100, None)}, ('D', 'FEMALE'): {2000: (20, 6), 2001: (30, None), 2002: (60, 5), 2003: (80, None)}, ('E', 'FEMALE'): {2000: (70, 3), 2001: (90, None), 2002: (20, 6), 2003: (10, None)}, ('F', 'FEMALE'): {2000: (40, 4), 2001: (40, None), 2002: (70, 4), 2003: (50, None)}})
	def test_rank_names_for_one_year_8 (self):
		"""call on all years of a database."""
		d = copy.deepcopy(ud10)
		rank_names_for_one_year(d,2000)
		rank_names_for_one_year(d,2001)
		rank_names_for_one_year(d,2002)
		rank_names_for_one_year(d,2003)
		self.assertEqual(d,rd10)
	
	def test_rank_names_1 (self): d = copy.deepcopy(ud1); rank_names(d); self.assertEqual(d,rd1)
	def test_rank_names_2 (self): d = copy.deepcopy(ud2); rank_names(d); self.assertEqual(d,rd2)
	def test_rank_names_3 (self): d = copy.deepcopy(ud3); rank_names(d); self.assertEqual(d,rd3)
	def test_rank_names_4 (self): d = copy.deepcopy(ud4); rank_names(d); self.assertEqual(d,rd4)
	def test_rank_names_5 (self): d = copy.deepcopy(ud5); rank_names(d); self.assertEqual(d,rd5)
	def test_rank_names_6 (self): d = copy.deepcopy(ud6); rank_names(d); self.assertEqual(d,rd6)
	def test_rank_names_7 (self): d = copy.deepcopy(ud7); rank_names(d); self.assertEqual(d,rd7)
	def test_rank_names_8 (self): d = copy.deepcopy(ud10); rank_names(d); self.assertEqual(d,rd10)
	
	def test_popularity_by_name_1 (self): self.assertEqual(popularity_by_name(rd2,"DANIEL","MALE"),[(2009, 1), (2010, 1), (2011, 1), (2012, 1)])
	def test_popularity_by_name_2 (self): self.assertEqual(popularity_by_name(rd3,"AMY","FEMALE"),[(2010, 1), (2011, 2), (2012, 1)])
	def test_popularity_by_name_3 (self): self.assertEqual(popularity_by_name(rd3,"BEA","FEMALE"),[(2010, 2), (2011, 1), (2012, 2)])
	def test_popularity_by_name_4 (self): self.assertEqual(popularity_by_name(rd6,"S","MALE"),[(2010, 2), (2011, 1), (2012, 1), (2013, 3)])
	def test_popularity_by_name_5 (self): self.assertEqual(popularity_by_name(rd4,"ALI","MALE"),[(2011, 1), (2012, 1), (2013, 1), (2014, 1), (2015, 1)])
	def test_popularity_by_name_6 (self): self.assertEqual(popularity_by_name(rd10,"A","FEMALE"),[(2000, 1), (2001, 3), (2002, 1), (2003, 2)])
	def test_popularity_by_name_7 (self): self.assertEqual(popularity_by_name(rd10,"B","FEMALE"),[(2000, 2), (2001, 6), (2002, 3), (2003, 1)])
	def test_popularity_by_name_8 (self): self.assertEqual(popularity_by_name(rd10,"C","FEMALE"),[(2000, 5), (2001, 1), (2002, 2), (2003, 5)])
	
	def test_popularity_by_year_1 (self): self.assertEqual(popularity_by_year(rd5,"FEMALE",2015,top=1),[(1, 'A')])
	def test_popularity_by_year_2 (self): self.assertEqual(popularity_by_year(rd5,"FEMALE",2015,top=3),[(1, 'A'), (2, 'B'), (3, 'C')])
	def test_popularity_by_year_3 (self): self.assertEqual(popularity_by_year(rd5,"FEMALE",2015      ),[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'F'), (7, 'G'), (8, 'H'), (9, 'I'), (10, 'J')])
	def test_popularity_by_year_4 (self): self.assertEqual(popularity_by_year(rd5,"FEMALE",2015,top=25),[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'F'), (7, 'G'), (8, 'H'), (9, 'I'), (10, 'J'), (11, 'K'), (12, 'L'), (13, 'M'), (14, 'N'), (15, 'O'), (16, 'P'), (17, 'Q'), (18, 'R'), (19, 'S'), (20, 'T')])
	def test_popularity_by_year_5 (self): self.assertEqual(popularity_by_year(rd8,"MALE",2011,4),[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (4, 'E')])
	def test_popularity_by_year_6 (self): self.assertEqual(popularity_by_year(rd9,"FEMALE",2000,top=5),[(1, 'M'), (2, 'N'), (3, 'O'), (4, 'P'), (5, 'Q')])
	def test_popularity_by_year_7 (self): self.assertEqual(popularity_by_year(rd6,"MALE",2013,top=5),[(1, 'X'), (2, 'T'), (3, 'S'), (3, 'Y'), (5, 'V')])
	def test_popularity_by_year_8 (self): self.assertEqual(popularity_by_year(rd6,"MALE",2013),[(1, 'X'), (2, 'T'), (3, 'S'), (3, 'Y'), (5, 'V'), (6, 'W'), (7, 'U')])
	
	def test_always_popular_names_1 (self): self.assertEqual(always_popular_names(rd10,"FEMALE",[2000,2001,2002,2003],top=3),['A'])
	def test_always_popular_names_2 (self): self.assertEqual(always_popular_names(rd10,"FEMALE",[2000,2001,2002,2003],top=4),['A', 'F'])
	def test_always_popular_names_3 (self): self.assertEqual(always_popular_names(rd10,"FEMALE",[2000,2001],top=4),['A', 'E', 'F'])
	def test_always_popular_names_4 (self): self.assertEqual(always_popular_names(rd10,"FEMALE",top=6),['A', 'B', 'C', 'D', 'E', 'F'])
	def test_always_popular_names_5 (self): self.assertEqual(always_popular_names(rd10,"FEMALE"),['A', 'B', 'C', 'D', 'E', 'F'])
	def test_always_popular_names_6 (self): self.assertEqual(always_popular_names(rd8,"MALE",top=3),['B'])
	def test_always_popular_names_7 (self): self.assertEqual(always_popular_names(rd7,"MALE",[2012],top=2),[])
	def test_always_popular_names_8 (self): self.assertEqual(always_popular_names(rd0,"MALE",[2009,2010,2011],top=3),['DANIEL'])
	
	def test_increasing_rank_names_1 (self): self.assertEqual(increasing_rank_names(rd0,"MALE",2009,2011),['JACOB', 'MATTHEW'])
	def test_increasing_rank_names_2 (self): self.assertEqual(increasing_rank_names(rd2,"MALE",2011,2012),['BART'])
	def test_increasing_rank_names_3 (self): self.assertEqual(increasing_rank_names(rd3,"FEMALE",2011,2012),['AMY'])
	def test_increasing_rank_names_4 (self): self.assertEqual(increasing_rank_names(rd3,"MALE",2010,2012),[]) # no males in this database!
	def test_increasing_rank_names_5 (self): self.assertEqual(increasing_rank_names(rd6,"MALE",2010,2013),['T'])
	def test_increasing_rank_names_6 (self): self.assertEqual(increasing_rank_names(rd10,"FEMALE",2000,2003),['B', 'D'])
	def test_increasing_rank_names_7 (self): self.assertEqual(increasing_rank_names(rd10,"FEMALE",2001,2003),['A', 'B', 'D'])
	def test_increasing_rank_names_8 (self): self.assertEqual(increasing_rank_names(rd10,"FEMALE",2000,2002),['C', 'D'])
	
	def test_extra_credit_merge_databases_1(self):
		d = {('CAT', 'FEMALE'): {2010: (300, 3), 2011: (200, None), 2012: (200, None)}}
		e = {('CAT', 'FEMALE'): {2013: (400, 3), 2014: (500, None), 2015: (600, None)}}
		ans = {('CAT', 'FEMALE'): {2010: (300, 1), 2011: (200, 1), 2012: (200, 1), 2013: (400, 1), 2014: (500, 1), 2015: (600, 1)}}
		self.assertEqual(merge_databases(d,e),ans)
	def test_extra_credit_merge_databases_2(self):
		d = {('CAT', 'FEMALE'): {2010: (300, 3), 2011: (200, None), 2012: (200, None)}}
		e = {('DOG', 'FEMALE'): {2013: (400, 3), 2014: (500, None), 2015: (600, None)}}
		ans = {('DOG', 'FEMALE'): {2013: (400, 1), 2014: (500, 1), 2015: (600, 1)}, ('CAT', 'FEMALE'): {2010: (300, 1), 2011: (200, 1), 2012: (200, 1)}}
		self.assertEqual(merge_databases(d,e),ans)
	def test_extra_credit_merge_databases_3(self):
		d = rd10
		e = rd6
		ans = {('S', 'MALE'): {2010: (10, 2), 2011: (10, 1), 2012: (10, 1), 2013: (10, 3)}, ('E', 'FEMALE'): {2000: (70, 3), 2001: (90, 2), 2002: (20, 6), 2003: (10, 6)}, ('Y', 'MALE'): {2012: (10, 1), 2013: (10, 3)}, ('C', 'FEMALE'): {2000: (30, 5), 2001: (100, 1), 2002: (90, 2), 2003: (20, 5)}, ('U', 'MALE'): {2010: (15, 1), 2011: (10, 1), 2012: (5, 7), 2013: (1, 7)}, ('V', 'MALE'): {2012: (10, 1), 2013: (5, 5)}, ('W', 'MALE'): {2012: (10, 1), 2013: (4, 6)}, ('X', 'MALE'): {2012: (10, 1), 2013: (13, 1)}, ('A', 'FEMALE'): {2000: (100, 1), 2001: (80, 3), 2002: (100, 1), 2003: (90, 2)}, ('F', 'FEMALE'): {2000: (40, 4), 2001: (40, 4), 2002: (70, 4), 2003: (50, 4)}, ('B', 'FEMALE'): {2000: (90, 2), 2001: (10, 6), 2002: (80, 3), 2003: (100, 1)}, ('D', 'FEMALE'): {2000: (20, 6), 2001: (30, 5), 2002: (60, 5), 2003: (80, 3)}, ('T', 'MALE'): {2010: (8, 3), 2011: (9, 3), 2012: (10, 1), 2013: (11, 2)}}
		self.assertEqual(merge_databases(d,e),ans)
	def test_extra_credit_merge_databases_4(self):
		d = rd2
		e = rd3
		ans = {('DANIEL', 'MALE'): {2009: (400, 1), 2010: (425, 1), 2011: (450, 1), 2012: (475, 1)}, ('HIGHLANDER', 'MALE'): {2011: (1, 5)}, ('AMY', 'FEMALE'): {2010: (500, 1), 2011: (400, 2), 2012: (500, 1)}, ('BART', 'MALE'): {2011: (300, 3), 2012: (400, 2)}, ('CHASE', 'MALE'): {2011: (350, 2), 2012: (325, 3)}, ('ZUUL', 'MALE'): {2011: (2, 4)}, ('CAT', 'FEMALE'): {2010: (300, 3), 2011: (200, 3), 2012: (200, 3)}, ('BEA', 'FEMALE'): {2010: (400, 2), 2011: (500, 1), 2012: (400, 2)}}
		self.assertEqual(merge_databases(d,e),ans)
	def test_extra_credit_merge_databases_5(self):
		d = merge_databases(rd0,rd1)
		d = merge_databases(d,rd2)
		d = merge_databases(d,rd3)
		d = merge_databases(d,rd4)
		d = merge_databases(d,rd5)
		d = merge_databases(d,rd6)
		d = merge_databases(d,rd7)
		d = merge_databases(d,rd8)
		d = merge_databases(d,rd9)
		d = merge_databases(d,rd10)
		ans = {('JACOB', 'MALE'): {2009: (2978, 4), 2010: (3368, 2), 2011: (3180, 2)}, ('H', 'MALE'): {2000: (19, 8)}, ('T', 'FEMALE'): {2000: (7, 14), 2015: (1, 20)}, ('W', 'MALE'): {2012: (10, 6), 2013: (4, 9)}, ('D', 'MALE'): {2000: (23, 4), 2011: (60, 17)}, ('H', 'FEMALE'): {2015: (13, 8)}, ('J', 'FEMALE'): {2015: (11, 10)}, ('X', 'MALE'): {2012: (10, 6), 2013: (13, 4)}, ('ALEXANDER', 'MALE'): {2009: (2905, 5), 2010: (2619, 4), 2011: (2494, 5)}, ('G', 'FEMALE'): {2015: (14, 7)}, ('HIGHLANDER', 'MALE'): {2011: (1, 23)}, ('U', 'FEMALE'): {2000: (6, 15)}, ('BHARAT', 'MALE'): {20: (17, 3)}, ('X', 'FEMALE'): {2000: (3, 18)}, ('L', 'MALE'): {2000: (15, 12)}, ('R', 'FEMALE'): {2000: (9, 12), 2015: (3, 18)}, ('ZUUL', 'MALE'): {2011: (2, 22)}, ('C', 'MALE'): {2000: (24, 3), 2009: (90, 11), 2010: (90, 11), 2011: (70, 16)}, ('U', 'MALE'): {2010: (15, 14), 2011: (10, 19), 2012: (5, 12), 2013: (1, 10)}, ('O', 'FEMALE'): {2000: (12, 9), 2015: (6, 15)}, ('ANTHONY', 'MALE'): {2009: (3106, 2), 2010: (2882, 3), 2011: (2716, 4)}, ('E', 'MALE'): {2000: (22, 5), 2011: (60, 17)}, ('CAT', 'FEMALE'): {2010: (300, 3), 2011: (200, 3), 2012: (200, 3)}, ('A', 'FEMALE'): {2000: (100, 1), 2001: (80, 3), 2002: (100, 1), 2003: (90, 2), 2011: (100, 4), 2012: (50, 4), 2013: (1000, 1), 2015: (20, 1)}, ('Q', 'FEMALE'): {2000: (10, 11), 2015: (4, 17)}, ('JAYDEN', 'MALE'): {2010: (2460, 7), 2011: (2773, 3)}, ('F', 'FEMALE'): {2000: (40, 4), 2001: (40, 4), 2002: (70, 4), 2003: (50, 4), 2015: (15, 6)}, ('P', 'FEMALE'): {2000: (11, 10), 2015: (5, 16)}, ('ANGEL', 'MALE'): {2009: (3058, 3), 2010: (2581, 5)}, ('JEFF', 'MALE'): {2014: (200, 1)}, ('F', 'MALE'): {2000: (21, 6), 2011: (1, 23)}, ('DOUG, JR', 'MALE'): {20: (10, 4)}, ('LUKE', 'MALE'): {2013: (200, 1), 2015: (200, 1)}, ('T', 'MALE'): {2010: (8, 16), 2011: (9, 21), 2012: (10, 6), 2013: (11, 5)}, ('I', 'MALE'): {2000: (18, 9)}, ('S', 'MALE'): {2010: (10, 15), 2011: (10, 19), 2012: (10, 6), 2013: (10, 6)}, ('V', 'MALE'): {2012: (10, 6), 2013: (5, 8)}, ('Y', 'MALE'): {2012: (10, 6), 2013: (10, 6)}, ('A', 'MALE'): {2000: (26, 1), 2010: (90, 11), 2011: (90, 14)}, ('B', 'FEMALE'): {2000: (90, 2), 2001: (10, 6), 2002: (80, 3), 2003: (100, 1), 2012: (10, 5), 2015: (19, 2)}, ('CHASE', 'MALE'): {2011: (350, 11), 2012: (325, 3)}, ('V', 'FEMALE'): {2000: (5, 16)}, ('I', 'FEMALE'): {2015: (12, 9)}, ('QUINCY, III', 'MALE'): {20: (8, 5)}, ('B', 'MALE'): {2008: (90, 1), 2009: (90, 11), 2010: (90, 11), 2011: (80, 15), 2000: (25, 2)}, ('ETHAN', 'MALE'): {2009: (2687, 6), 2010: (2497, 6), 2011: (2408, 7)}, ('BART', 'MALE'): {2011: (300, 12), 2012: (400, 2)}, ('C', 'FEMALE'): {2000: (30, 5), 2001: (100, 1), 2002: (90, 2), 2003: (20, 5), 2012: (10, 5), 2015: (18, 3)}, ('JOSHUA', 'MALE'): {2009: (2435, 9)}, ('N', 'FEMALE'): {2000: (13, 8), 2015: (7, 14)}, ('W', 'FEMALE'): {2000: (4, 17)}, ('BEA', 'FEMALE'): {2010: (400, 2), 2011: (500, 1), 2012: (400, 2)}, ('K', 'FEMALE'): {2015: (10, 11)}, ('E', 'FEMALE'): {2000: (70, 3), 2001: (90, 2), 2002: (20, 6), 2003: (10, 6), 2015: (16, 5)}, ('BOB', 'MALE'): {2012: (200, 4), 2013: (200, 1), 2014: (200, 1)}, ('MATTHEW', 'MALE'): {2009: (2435, 9), 2011: (2490, 6)}, ('NATHAN', 'MALE'): {2010: (2286, 10), 2011: (2261, 10)}, ('M', 'FEMALE'): {2000: (14, 7), 2015: (8, 13)}, ('S', 'FEMALE'): {2000: (8, 13), 2015: (2, 19)}, ('DANIEL', 'MALE'): {2009: (3823, 1), 2010: (3600, 1), 2011: (3386, 1), 2012: (475, 1)}, ('D', 'FEMALE'): {2000: (20, 6), 2001: (30, 5), 2002: (60, 5), 2003: (80, 3), 2012: (5, 7), 2015: (17, 4)}, ('DAVID', 'MALE'): {2009: (2648, 7), 2010: (2442, 8), 2011: (2324, 8), 20: (24, 1)}, ('CHAD', 'MALE'): {20: (6, 6)}, ('L', 'FEMALE'): {2015: (9, 12)}, ('ANDREW', 'MALE'): {2009: (2605, 8), 2010: (2391, 9), 2011: (2310, 9)}, ('K', 'MALE'): {2000: (16, 11)}, ('ALI', 'MALE'): {20: (20, 2), 2011: (200, 13), 2012: (200, 4), 2013: (200, 1), 2014: (200, 1), 2015: (200, 1)}, ('G', 'MALE'): {2000: (20, 7)}, ('AMY', 'FEMALE'): {2010: (500, 1), 2011: (400, 2), 2012: (500, 1)}, ('EGGBERT', 'MALE'): {20: (2, 7)}, ('J', 'MALE'): {2000: (17, 10)}}
		self.assertEqual(d,ans)
	
# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		# find all methods that begin with "test".
		fs = []
		for w in wants:
			for func in AllTests.__dict__:
				# append regular tests
				# drop any digits from the end of str(func).
				dropnum = str(func)
				while dropnum[-1] in "1234567890":
					dropnum = dropnum[:-1]
				
				if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
					fs.append(AllTests(str(func)))
				if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
					fs.append(AllTests(str(func)))
		
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self,wants):
			# find all methods that begin with "test".
			fs = []
			for w in wants:
				for func in AllTests.__dict__:
					if BATCH_MODE and str(func).startswith("test_extra_credit_"+w):
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
			else:
				raise Exception("asked to limit testing to unknown function '%s'."%w)
	else:
		wants = REQUIRED_DEFNS
		
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
		except FileNotFoundError as e:
			return (filename+"_FILE_NOT_FOUND_ERROR",0,1)
		except Exception as e:
			return (filename+str(e.__reduce__()[0]),0,1)
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
