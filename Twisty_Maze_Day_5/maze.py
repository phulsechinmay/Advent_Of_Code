'''
=============================================
This is a solution script to the Day 5 problem of Advent Of Code. Part 1 is supposed to find the number of steps required to get out of a maze of CPU jump
instructions, where the jump offset is given by the number at that index in a list. In addition, every jump we do adds 1 to the number at the point in the
list where we jumped from

Solution complexity: O(n) where m is number of steps

Part 2 has another condition, where if the offeset is greater than or equal to three, it is reduced by one instead of incremented. 

Solution complexity: O(m) where m is the number of steps required

I am pretty sure there is a more efficient way of doing this, I'm currently working on it. Targeting O(n) if possible, atleast for part 1. 
=============================================
'''


fileName = input('Please enter the filename: ')

maze = open(fileName).read().splitlines()

index = 0;

steps = 0;

while (index >= 0) and (index < len(maze)):
	num = int(maze[index])
	maze[index] = num+1
	index += num
	steps += 1

print("Part 1: Number of steps needed: %d" % (steps))

index = 0

steps = 0

maze = open(fileName).read().splitlines()

while (index >= 0) and (index < len(maze)):
	num = int(maze[index])
	if num >= 3 :
		maze[index] = num - 1
	else:
		maze[index] = num + 1
	index += num
	steps += 1

print("Part 2: Number of steps needed: %d" % (steps))