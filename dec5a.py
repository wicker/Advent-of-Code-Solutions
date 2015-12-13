# naughty or nice strings

from sys import argv
import hashlib

script, filename = argv

s = open(filename).read().splitlines()

nice_set = ['a','e','i','o','u']
nice = False
count = 0

for line in s:
	prev_c = 'False'
	nice = False
	vowel_check = 0
	repeat_check = 0
	order_check = 0
	for c in line: 
		if c in nice_set:
			vowel_check = vowel_check + 1
		if prev_c == c:
			repeat_check = repeat_check + 1
		if (prev_c == 'a' and c == 'b') or (prev_c == 'c' and c == 'd') or (prev_c == 'p' and c == 'q') or (prev_c == 'x' and c == 'y'):
			order_check = order_check + 1
		prev_c = c
	if vowel_check >= 3 and repeat_check >= 1 and order_check == 0:
		count = count + 1
		print line

print count

