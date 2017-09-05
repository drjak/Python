#!/usr/bin/python

import random
print ('I will flip coin 1000 times. Guess how many times head comes up (enter to begin)')
input()
flips=0
heads=0

while flips < 1000:
	if random.randint(0,1) == 1:
		heads = heads+1
	flips = flips+1

	if flips == 900:
		print ('900 flips and there have been '+str(heads) + ' heads')
	if flips == 100:
		print ('At 100 tosses, heads has come up '+str(heads)+' so far')
	if flips == 500:
		print ('Half way done and heads: '+str(heads))

print()
print ('Out of 1000 coin tosses, head came up '+ str(heads)+ ' times')	
