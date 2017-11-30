#this is the main file
import module_one


randdmg = 10

z = []

with open('playerstats.txt') as f:
	for line in f:
		z.append(line)

#print(z)
print("this is your hp:",float(z[0]))
print("you take",randdmg,"damage for no reason: haha")

new_val = float(z[0])-randdmg

with open("playerstats.txt", "w") as f:
	writeset = str(new_val)+"\n3\n5"
	f.write(writeset)

with open("playerstats.txt") as f:
	z = f.readlines()

print("this is your new hp:",z[0])


#works
print("Oh no! An ugly ass troll appears in front of you")
print("He attacks you!")
x = input("Do you want to take full damage or attempt to block?: (y/n)")
if x == "y":
	f = open("playerstats.txt")
	z = f.readlines()
	f.close()
	taken_damage = ((randdmg/2)*1.5)-float(z[2])
	new_hp_val = float(z[0])-taken_damage
	print("Your armor class is currently:",z[2])
	print("Due to armor mitigation you only take:",taken_damage)
	with open("playerstats.txt","w") as f:
		writeset = str(new_hp_val)+"\n3\n5"
		f.write(writeset)
	print("stats updated...")
elif x == "n":
	print("welp nothing happens yet because i'm tired and going to bed")
	print("also, what a terrible choice...sigh people these days")
else:
	print("haha, you're so dumb you couldn't even yes or no. You die.")
	print(z)
	uh = module_one.reset_hp(-20)
