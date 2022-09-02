#!/usr/bin/python

"""
Given results of Wordle guesses, show remaining possible words.
"""

word_list = set()
with open("wordle_dict.txt","r") as infile:
	word_list = { line.strip() for line in infile.readlines() }

contains = set() # yellow letters
excludes = set() # black letters
pos_matches = [None,None,None,None,None] # green letters
neg_matches = set() # letter/position values that are yellow

def matches(word):
	# Deal with edge case where a second of the same letter is greyed out
	for entry in contains:
		excludes.discard(entry)
	# Not a match if it contains black letters
	if len(set(word).intersection(excludes)) > 0:
		return False
	# Not a match if it doesn't contain all green letters
	if not contains.issubset(set(word)):
		return False
	# Not a match if it doesn't have green letters in the right place
	for idx,val in enumerate(pos_matches):
		if val != None and word[idx] != val:
			return False
	# Not a match if the right letter is in the wrong place
	for match in neg_matches:
		if word[match[1]] == match[0]:
			return False
	return True

while True:
	for idx in range(5):
		val = input("Enter letter at " + str(idx+1) + " ")
		col = input("Enter color of letter: (Y,B,G) ")
		val = val.lower()
		col = col.upper()
		if col == 'B':
			excludes.add(val)
		elif col == 'Y':
			contains.add(val)
			neg_matches.add((val,idx))
		elif col == 'G':
			contains.add(val)
			pos_matches[idx] = val
	word_list = { word for word in word_list if matches(word) }
	print("Remaining words: ",sorted(word_list))




