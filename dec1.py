from sys import argv

script, filename = argv

s = open(filename).read()

floor = 0
count = 0

for i in s:
	if floor == -1:
	  break
	if i == '(':
		floor = floor + 1
	elif i == ')':
		floor = floor - 1
	count = count + 1

print floor
print count
