
class Grade:
	def __init__(self, kind, name, percent):
		
		self.kind = kind
		self.name = name
		self.percent = percent
		#if kind != "test" or kind != "lab" or kind != "project" or kind != "final":
			#raise GradingError("no Grade kind",kind+".")
		
	def __str__(self):
		return ("%s:%s(%d%%)" % (self.kind, self.name, self.percent))
		
	def __repr__(self):
		return ("Grade('%s', '%s', %d)" % (self.kind, self.name, self.percent))

	def __eq__(self, other):
		return self.kind == other.kind and self.name==other.name and self.percent == other.percent

class GradeBook:
	def __init__(self):
		self.grades = []
		
	def __str__(self):
		ans = "GradeBook:\n"
		for line in self.grades:
			ans += "\t"+str(line)+"\n"
		return ans
		
	def __repr__(self):
		return (str(self))
		
	def add_grade(self, grade):
		self.grades.append(grade)
		
	def average_by_kind(self, kind):
		total = 0
		allgrades = 0
		for each in self.grades:
			print(each)
			'''
			if each[0] == self.kind:
				total += 1
				allgrades += each[2]
		if allgrades == 0:
			ans = None
		else:
			ans = allgrades/total
		return ans
		'''
	def get_all_of(self, kind):
		all_of_kind = []
		for each in self.grades:
			if each[0] == self.kind:
				all_of_kind.append(each)
		return all_of_kind
		
	def get_by_name(self, name):
		all_of_name = []
		for each in self.grades:
			if each[1] == self.name:
				if len(all_of_name) < 0:
					all_of_name.append(each)
				elif len(all_of_name) >= 1:
					break
		if all_of_name == []:
			raise GradingError("no Grade found named",self.name)
		return all_of_name

