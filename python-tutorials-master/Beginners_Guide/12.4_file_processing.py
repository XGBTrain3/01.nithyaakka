txt = open("exercises.txt")

for line in txt.readlines():
	if "circle" in line:
		print "Found circle"
		print line	
txt.close()

