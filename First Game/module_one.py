#module 1.0
def reset_hp(y):
	if y <= 0:
		reset = "100\n3\n5"
	print("you are dead, game will reset:")
	
	with open("playerstats.txt", "w") as f:
	
		f.write(reset)
	print("hp resetted")
	return None