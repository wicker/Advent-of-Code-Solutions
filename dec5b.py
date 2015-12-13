# naughty or nice strings
# part 2

from sys import argv
import hashlib

script, filename = argv

s = open(filename).read().splitlines()

nice = False
count = 0

for line in s:
	prev1_c = 'False'
	prev2_c = 'False'
	nice = False
	check1 = 0
	check2 = 0
	for c in line: 
		if line.count(prev1_c+c) > 1:
			check1 = check1 + 1
		if prev2_c == c:
			check2 = check2 + 1
		prev2_c = prev1_c
		prev1_c = c
	if check1 > 0 and check2 > 0:
		count = count + 1
		print line

print count

