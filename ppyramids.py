#!/usr/bin/env python

#change

#input word for the text
text = input("What word do you want to print? --> ")
space = " "

#fixed width in characters
width = 181
r = int(width/len(text))

#number of pyramids
repetition = int(input("How many repetitions? --> "))

for i in range(repetition):
	for i in range(r+1):
		print(text*i)

	for i in range(r-1):
		print(text*(r-i-1), end=" ")
		print(space*i)