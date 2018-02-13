'''
=============================================
This is a solution script to the Day 2 problem of Advent Of Code. Part 1 is supposed to find the difference between the largest and smallest value in a row
and add up all the differences
=============================================
'''

file = open("test.txt")
row = 0;
col = 0;

with open("test.txt") as f:
	for i,l in enumerate(f):
		row += 1
		listrow = [int(i) for i in l.split()];
		col = len(listrow)

matrix = [[0 for x in range(col)] for y in range(row)]

for i,l in enumerate(file):
	matrix[i] = [int(i) for i in l.split()];

sum = 0

for row in matrix:
	sum += max(row) - min(row)

print("Part 1: The sum of differences is %d" % (sum))

# Part 2: The goal is to find the two evenly divisible numbers in a row and find the quotient and then add the quotients up

sum2 = 0

for row in matrix:
	for num in row:
		evenquotients = [(x//num) for x in row if x%num == 0]
		if(len(evenquotients) > 1):
			evenquotients.remove(1)
			sum2 += evenquotients[0]
			break

print("Part 2: The sum of the even quotients is %d" % (sum2))