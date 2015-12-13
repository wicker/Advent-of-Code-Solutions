# christmas lights 

from sys import argv
import hashlib

script, filename = argv

def ToggleGrid(x1,y1,x2,y2):
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			light_grid[i][j] = not light_grid[i][j]

def TurnOff(x1,y1,x2,y2):
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			light_grid[i][j] = False;

def TurnOn(x1,y1,x2,y2):
	for i in range(x1,x2+1):
		for j in range(y1,y2+1):
			light_grid[i][j] = True;

light_grid = [[False for x in range(0,1000)] for y in range(0,1000)]

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
		if light_grid[x][y] == True:
			count = count + 1

print count
