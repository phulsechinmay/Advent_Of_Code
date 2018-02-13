'''
=============================================
This is a solution script to the Day 4 problem of Advent Of Code. Part 1 is supposed to find the number of valid passphrases, where an invalid passphrase contains
a word that had already been in the passphrase.

Solution complexity: O(n) where n is number of words

Part 2 has another condition for an invalid passphrase, where it's invalid if it contains words that are anagrams of each other

Solution complexity: O(m log(m)) where m is the number of characters in the passphrase. This is mainly due to sorting every word in the passphrase
=============================================
'''

fileName = input("Please enter the filename: ")

file = open(fileName)

partOneCountValid = 0
partTwoCountValid = 0

for line in file :
	line = line.strip()
	partOneValid = True
	partTwoValid = True
	wordsUsedPartOne = {}
	wordsUsedPartTwo = {}
	words = line.split(' ')
	for word in words :
		wordValue = 0
		sortedWord = ''.join(sorted(word))
		if sortedWord in wordsUsedPartTwo :
			partTwoValid = False
		else :
			wordsUsedPartTwo[sortedWord] = True
		if word in wordsUsedPartOne :
			partOneValid = False
			partTwoValid = False
			break
		else :
			wordsUsedPartOne[word] = True

	if partOneValid == True:
		partOneCountValid += 1
	if partTwoValid == True:
		partTwoCountValid += 1


print("Part 1: Number of valid passcodes: %d" % (partOneCountValid))

print("Part 2: Number of valid passcodes: %d" % (partTwoCountValid))
