#!/bin/python
#
# This is a modified sample code on the Programming for Everyone (Python) provided by Michigan Univ.
# Here is a link to this course: https://www.coursera.org/course/pythonlearn
# How to use: 
# Step1. $python wordcount.py
# Step2. input a target text file like word.txt
# Result using word.txt 
# most common word/count: week / 10 
# most uncommon word/count: Functions / 1
# Have a enjoy!

#define find the most common word
def findMostCommonWord(word, counts):
	bigcount = None
	bigword = None
	for word, count in counts.items():
			if bigcount is None or count>bigcount: 
				bigword = word
				bigcount = count	
 	return bigcount, bigword
	 
#define fine the most uncommon word
def findMostUncommonWord(word, counts):
	smallcount = None
	smallword = None
	for word, count in counts.items():
			if smallcount is None or count<smallcount: 
				smallword = word
				smallcount = count	
 	return smallcount, smallword
	
 
#Get the name of the file and open it
name = raw_input("Enter File: ")
handle = open(name, "r")
text = handle.read()
words = text.split()

# Count word frequency
counts = dict()
for word in words:
	counts[word] = counts.get(word, 0) + 1

#find the most common&uncommon word 
bigcount = None
bigword = None
smallcount = None
smallword = None
bigcount, bigword     = findMostCommonWord(word, counts)
smallcount, smallword = findMostUncommonWord(word, counts)

# All done
print bigword, bigcount
print smallword, smallcount
