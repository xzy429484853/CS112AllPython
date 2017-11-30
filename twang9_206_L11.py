#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Project 3
# Lab Section 206
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: python documentation, zyante exercises 1-14
#-------------------------------------------------------------------------------
# Comments and assumptions:
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
class Grade:
	def __init__(self, kind, name, percent):
		#set kind to this instance self
		self.kind = kind
		#set name to this instance self
		self.name = name
		#set percent to this instance self
		self.percent = percent
		#check if kind is test
		if kind != "test":
			#check kind is lab
			if kind != "lab":
				#check kind is project
				if kind != "project":
					#check is kind final
					if kind != "final":
						#since not any, raise GradingError
						raise GradingError("no Grade kind '%s'" % kind)
		
	def __str__(self):
		#return human-centric string Grade values
		return ("%s:%s(%d%%)" % (self.kind, self.name, self.percent))
		
	def __repr__(self):
		#return computer-centric string of values
		return ("Grade('%s', '%s', %d)" % (self.kind, self.name, self.percent))

	def __eq__(self, other):
		#check to see if each value is equal to other value
		return self.kind == other.kind and self.name==other.name and self.percent == other.percent

class GradeBook:
	def __init__(self):
		#make empty list self.grades
		self.grades = []
		
	def __str__(self):
		#add the first part to ans string
		ans = "GradeBook:\n"
		#for each value in list self.grades
		for line in self.grades:
			#add a tab then value then newline to ans list
			ans += "\t"+str(line)+"\n"
		#return human-centric string representation
		return ans
		
	def __repr__(self):
		#simply return the same as __str__
		return (str(self))
		
	def add_grade(self, grade):
		#add the given grade to self.grades list
		self.grades.append(grade)
		
	def average_by_kind(self, kind):
		#sum of grades as 0
		allgrades = 0
		#num of grades as 0
		total = 0
		#for each value in list self.grades
		for each in self.grades:
			#call object grade
			#s as eachobject kind value
			s = each.kind
			#if s is same as kind
			if s == kind:
				#x as eachobject percent value
				x = each.percent
				#add x to allgrades
				allgrades += x
				#add 1 to total grades
				total += 1
		#if allgrades is 0
		if allgrades == 0:
			#make list None
			ans = None
		#otherwise
		else:
			#find average as ans
			ans = allgrades/total
		#return ans
		return ans
		
	def get_all_of(self, kind):
		#empty list all_of_kind
		all_of_kind = []
		#each grade in self.grades
		for each in self.grades:
			#s as eachobject kind
			s = each.kind
			#if s same as kind
			if s == kind:
				#add grade each to all_of_kind
				all_of_kind.append(each)
		#return list of all grades of same kind
		return all_of_kind
		
	def get_by_name(self, name):
		#empty list all_of_name
		all_of_name = []
		#for each grade in self.grades
		for each in self.grades:
			#s as eachobject name value
			s = each.name
			#if s same as name
			if s == name:
				#return this grade
				return each
		#if all_of_name is empty list
		if all_of_name == []:
			#raise GradingError of thatname
			raise GradingError("no Grade found named '%s'" % name)

class GradingError(Exception):
	def __init__(self,msg):
		#make msg as self.msg variable
		self.msg = msg
		
	def __str__(self):
		#simply return printed statement of self.msg
		return("%s" % self.msg)
		
	def __repr__(self):
		#return computer-centric string message of GradeingError with self.msg in triple quotes
		return("GradingError('''%s''')" % self.msg)
		