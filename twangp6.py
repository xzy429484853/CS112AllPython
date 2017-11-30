
import random

class Tile:
	def __init__(self,value):
		self.value = value

	def __str__(self):
		if self.value >= 10:
			return ("%d" % self.value)
		elif self.value < 10 and self.value > 0:
			return (" %d" % self.value)
		elif self.value == None:
			return ("<>")
		#return ("%2s" % (value))
		#return ("{:>2}".format(value))

	def __repr__(self):
		if self.value == None:
			return ("Tile(None)")
		else:
			return ("Tile(%d)" % self.value)

class Direction:
	def __init__(self,value):
		if value == "UP" or value == "DOWN" or value == "LEFT" or value == "RIGHT":
			self.value = value
		else:
			raise TileError("invalid value for %s" % value)

	def __str__(self):
		return ("%s" % self.value)
		
	def __repr__(self):
		return ("Direction('%s')" % self.value)

	def __eq__(self,other):
		return self.value == other.value

UP = Direction("UP")
DOWN = Direction("DOWN")
LEFT = Direction("LEFT")
RIGHT = Direction("RIGHT")
dirs = [UP,DOWN,LEFT,RIGHT]

class TileError(Exception):
	def __init__(self,msg):
		self.msg = msg

	def __str__(self):
		return self.msg

	def __repr__(self):
		return ("""TileError('''%s''')""" % self.msg)


class Puzzle:
	def __init__(self, grid=None, height=4, width=4):
		pass
	def __str__(self):
		pass
	def __repr__(self):
		pass
	def display(self):
		pass
	def find_opening(self):
		pass
	def move(self,dir):
		pass
	def is_solved(self):
		pass
	def scramble(self, n=1000):
		pass
	