# calculating wrapping paper
# my regex skills are pitiful

from sys import argv
from operator import add

script, filename = argv
total_area = 0
ribbon_total = 0

f = open(filename)
for line in f.readlines():
	# area of wrapping paper
	line = line.replace('x',' ')
	l,w,h = line.split(' ')
	l = int(l)
	w = int(w)
	h = int(h)
	sides = [2*l*w,2*w*h,2*h*l]
	total_area = total_area + reduce(add,sides,0) + min(sides)/2

	# length of ribbon 
	x = map(int, line.split())
	x = sorted(x)
	ribbon_present = x[0]*2 + x[1]*2
	ribbon_bow = l*w*h
	ribbon_total = ribbon_total + ribbon_present + ribbon_bow

f.close()
	
print "Total wrapping paper area:",total_area
print "Total ribbon length:",ribbon_total


