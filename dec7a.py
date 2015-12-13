# some assembly required part 1

from sys import argv
import hashlib

script, filename = argv

def ToggleGrid(x1,y1,x2,y2):
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			light_grid[i][j] += 2

def TurnOff(x1,y1,x2,y2):
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			if light_grid[i][j] > 0:
				light_grid[i][j] -= 1;

def TurnOn(x1,y1,x2,y2):
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			light_grid[i][j] += 1;

light_grid = [[0 for x in range(0,1000)] for y in range(0,1000)]

s = open(filename).read().splitlines()

for line in s:

	line = line.replace(',',' ')
	line = line.split(' ')
	if line[0] == 'toggle':
		ToggleGrid(int(line[1]),int(line[2]),int(line[4]),int(line[5]))
	elif line[1] == 'off':
		TurnOff(int(line[2]),int(line[3]),int(line[5]),int(line[6]))
	elif line[1] == 'on':
		TurnOn(int(line[2]),int(line[3]),int(line[5]),int(line[6]))

count = 0

for x in range(0,1000):
	for y in range(0,1000):
		count += light_grid[x][y]

print count
