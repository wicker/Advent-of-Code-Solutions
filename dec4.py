# md5 hash

from sys import argv
import hashlib

script, filename = argv

s = open(filename).read().splitlines()
d = 0

while True:
	d = d + 1
	a = str(d).zfill(6)
	s.append(a)
	b = ''.join(s)
	m = hashlib.md5(b.encode())
	if m.hexdigest()[:6] == '000000':
		print b
		break
	s.remove(a)



#grid = [(0,0)]
#s_x = 0
#s_y = 0
#rs_x = 0
#rs_y = 0
#toggle = True
#
#def updateHouse(i,a,b):
#	if i == 'v':
#		b = b - 1
#	elif i == '>':
#		a = a + 1
#	elif i == '^':
#		b = b + 1
#	elif i == '<':
#		a = a - 1
#	return (a,b)
#
#for i in s:	
#	print "i:",i,"santa:",(s_x,s_y),"robosanta:",(rs_x,rs_y)
#	if toggle == True:
#		(s_x,s_y) = updateHouse(i,s_x,s_y)
#		grid.append((s_x,s_y))
#		toggle = False
#	else:
#		(rs_x,rs_y) = updateHouse(i,rs_x,rs_y)
#		grid.append((rs_x,rs_y))
#		toggle = True
#
#houses = set(grid)
#print len(houses)
#
