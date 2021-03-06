'''
This is my solution script for Advent of Code Day 3, Spiral Memory. It heavily relies on just a mathematical formula, not doing any kind of matrix 
operations or iteration
'''
from math import *

dataPoint = input("Please enter the number to find the steps for: ")
dataPoint = int(dataPoint)

armLength = floor(sqrt(dataPoint)) if (floor(sqrt(dataPoint))%2 == 1) else ((sqrt(dataPoint)+1) if (sqrt(dataPoint)%2 == 0) else ceil(sqrt(dataPoint)))

closestOddSquare = armLength**2;

if(closestOddSquare<dataPoint):
	armLength += 1

difference = abs(closestOddSquare - dataPoint)

straightDistanceFromEntryPoint = int(floor(armLength/2)); # 

totalSteps = abs(straightDistanceFromEntryPoint - (difference % (straightDistanceFromEntryPoint*2))) + straightDistanceFromEntryPoint

print('The total number of steps is %d' % (totalSteps))

