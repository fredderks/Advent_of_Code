orbittest = [('COM','B'), (
'B','C'), (
'C','D'), (
'D','E'), (
'E','F'), (
'B','G'), (
'G','H'), (
'D','I'), (
'E','J'), (
'J','K'), (
'K','L')]

input = open('input.txt')
orbit = []
for line in input.readlines():
	line = str(line)
	line = line.replace("\n","")
	one = line[:3]
	two = line[4:]
	line = (one,two)
	orbit.append(line)

unique = []
for set in orbit:
	for i in set:
		if i not in unique:
			unique.append(i)
			
total_orbits = 0

set2 = []
for set in orbit:
	set2.append(set[1])

origin = None
for planet in unique:
	if planet not in set2:
		origin = planet
		print("Origin:",origin)	

for planet in unique[1:]:
	i = planet
	counter = 1
	lol = True
	while lol:
		for set in orbit:
			if set[1] == i:
				if set[0] == origin:
					print(set[1],'orbits',set[0],
					' - ',counter,'orbits\n')
					total_orbits += counter
					lol = False
				else:
					#print(set[1],'orbits',set[0])
					i = set[0]
					counter += 1
					break

print('\nTotal number of orbits:',total_orbits)