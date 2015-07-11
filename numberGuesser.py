#!/usr/bin/python
"""
NumberGuesser
	Guesses your number!

	Author: Greg Stewart
	Copyright 2014 Greg Stewart

	Start: 7/15/14

	Tries to guess your number, interacts with you via the Raspberry pi's 
		16x2 CharLCDPlate

It uses a relatively simple algorithm to guess numbers:
	
Step 1:
	Find a number that is larger than the user's number
		Does this by starting at 10, and multiplies it by 10 until
			the number is larger than the user's
		Also moves the lower boundary up to the last guess, as we know it is 
			higher than it already

Step 2:
	Find the halfway point between the upper and lower bounds, see if that is
		the number. If it isn't, see if it is high or low. Update the high/low
		bounds accordingly, and repeat until number is reached.
		
		Take the difference of the lower and upper bounds, then divide it by 2.
			Add this to the value of the lower bounds, and we have our next 
			guess, half way between the lower bounds .
		If not the correct number, prompt if the last guess is low or high.
			Based on this, set it to the high/low bounds as necessary.
		Repeat until desired number is reached.

"""
# print out program information
print "\n\nNumberGuesser\n\
Guesses a number that the user chooses\n\
Designed for use with the 16x2 Adafruit Character Plate\n\
\n\
Author: Greg Stewart\n\
Copyright 2014 Greg Stewart\n\
V 1.0\n\n" 

#imports
print "Importing needed modules..."
import time
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
print " Done.\n"

print "Setting up custom functions..."

#time waster between choices, as to not clog up input system
def okay():
	lcd.clear()
	lcd.message("Okay")
	time.sleep(.5)
	lcd.message(".")
	time.sleep(.5)
	lcd.message(".")
	time.sleep(.5)
	lcd.message(".")
	time.sleep(.5)

print " Done.\n"

print "Setting up Global variables..."
#
# Setup global variables
#

# Initialize the LCD plate.
lcd = Adafruit_CharLCDPlate(1)

# if we are going to be guessing
run = True

print " Done.\n"

print "Resetting Screen..."
# Clear display
lcd.clear()
lcd.backlight(lcd.OFF)
lcd.clear()
lcd.backlight(lcd.ON)

print " Done.\n"

#display beginnging informationals
print "Displaying welcome messages..."

lcd.message("NumberGuesser\nBy Greg Stewart")
time.sleep(2)

lcd.clear()
time.sleep(1)
lcd.message("Version:\n1.0")
time.sleep(2)

lcd.clear()
time.sleep(1)
lcd.message("Guesses your\nnumber!")
time.sleep(2)

lcd.clear()
time.sleep(1)
lcd.message("For \nScience!")
time.sleep(2)

print " Done.\n"

#loop for input, to see what to do next
#	SELECT exits the program, anything else starts the game
print "Waiting for player to decide on a number..."

lcd.clear()
time.sleep(1)

start = False
chosen = False
tempTime = time.time()
messArr = (("Think of a \npositive integer"),
		   ("To skip guessing\npress SELECT"),
		   ("Press anything\nelse to begin."))
messCounter = 0
lcd.message(messArr[messCounter])
#loop for input
while not start:
	if lcd.buttonPressed(lcd.SELECT):
		start = True
		print " Player chose to quit.\n"
	elif lcd.buttonPressed(lcd.UP) or lcd.buttonPressed(lcd.DOWN) or lcd.buttonPressed(lcd.LEFT) or lcd.buttonPressed(lcd.RIGHT):
		start = True
		chosen = True
		print " Player chose a number.\n"
	elif (time.time() - tempTime) >= 3:
		tempTime = time.time()
		lcd.clear()
		lcd.message(messArr[messCounter])
		messCounter += 1
		if messCounter > 2:
			messCounter = 0
	
lcd.clear()

#if not just exiting, play the game
if run and chosen:
	print "Begin Playing game:"
	print "\tShowing rules..."
	
	lcd.message("REMEMBER:")
	time.sleep(2)
	
	lcd.clear()
	lcd.message("UP = YES\nDOWN = NO")
	time.sleep(3)
	
	lcd.clear()
	lcd.message("RIGHT = Too High\nLEFT = Too Low")
	time.sleep(3)
	
	lcd.clear()
	lcd.message("SELECT = exit")
	time.sleep(3)
	
	print "\t Done.\n"
	
	playing = True
	turnCount = 0
	
	lastGuess = 10
	highGuess = lastGuess
	lowGuess = 0
	
	print "\tBegin trying to find player's number..."
	
	foundNum = False
	inStep = True
	answered = False
	#find a multiple of 10 that is larger than the number we are looking for
	while inStep and not foundNum:
		print "\t\tHighGuess: {0}\n\
\t\tlowGuess:  {1}\n\
\t\tlastGuess: {2}".format(highGuess,lowGuess,lastGuess)
		turnCount += 1
		answered = False
		
		lcd.clear()
		lcd.message("Is it:\n{0}".format(lastGuess))
		while not answered:
			if lcd.buttonPressed(lcd.UP):
				foundNum = True
				answered = True
			elif lcd.buttonPressed(lcd.DOWN):
				answered = True
			elif lcd.buttonPressed(lcd.SELECT):
				inStep = False
				answered = True
				run = False
				print "\tPlayer chose to end the game."
		if not foundNum and run:
			okay() 
		
		answered = False
		lcd.clear()
		lcd.message("{0}\nlow or high?".format(lastGuess))
		while not answered and not foundNum and run:
			if lcd.buttonPressed(lcd.RIGHT):#too high
				inStep = False
				answered = True
				highGuess = lastGuess
				print "\tFound upper bounds: {0}".format(highGuess)
				
			elif lcd.buttonPressed(lcd.LEFT):#too low
				answered = True
				lowGuess = lastGuess
				lastGuess *= 10
				highGuess = lastGuess
				print "\tFound another lower bounds: {0}".format(lowGuess)
			elif lcd.buttonPressed(lcd.SELECT):
				inStep = False
				answered = True
				run = False
				print "\tPlayer chose to end the game."
		if not foundNum and run:
			
			okay() 

	#Find the half-way between high and low and try to get closer
	inStep = True
	answered = False
		
	while inStep and not foundNum and run:
		print "\t\tHighGuess: {0}\n\
\t\tlowGuess:  {1}\n\
\t\tlastGuess: {2}".format(highGuess,lowGuess,lastGuess)
		lastGuess = lowGuess + ((highGuess - lowGuess)/2)
		turnCount += 1
		answered = False
		
		lcd.clear()
		lcd.message("Is it:\n{0}".format(lastGuess))
		while not answered:
			if lcd.buttonPressed(lcd.UP):
				foundNum = True
				answered = True
				
			elif lcd.buttonPressed(lcd.DOWN):
				answered = True
			elif lcd.buttonPressed(lcd.SELECT):
				inStep = False
				answered = True
				run = False
				print "\tPlayer chose to end the game."
		if not foundNum and run:
			okay() 
		
		answered = False
		lcd.clear()
		lcd.message("{0}\nlow or high?".format(lastGuess))
		while not answered and not foundNum and run:
			if lcd.buttonPressed(lcd.RIGHT):#too high
				answered = True
				highGuess = lastGuess
				print "\tFound another upper bounds: {0}".format(highGuess)
			elif lcd.buttonPressed(lcd.LEFT):#too low
				answered = True
				lowGuess = lastGuess
				print "\tFound another lower bounds: {0}".format(lastGuess)
			elif lcd.buttonPressed(lcd.SELECT):
				inStep = False
				answered = True
				run = False
				print "\tPlayer chose to end the game."
		if not foundNum and run:
			
			okay() 
	
	if foundNum:
		print "\tFound it! {0}".format(lastGuess)
		print "\tNumber of guesses: {0}".format(turnCount)
		print "\tDisplaying Stats..."
		lcd.clear()
		lcd.message("I guessed it!\n{0}".format(lastGuess))
		time.sleep(3)
		
		lcd.clear()
		lcd.message("# of guesses:\n{0}".format(turnCount))
		time.sleep(3)
		print "\t Done."
		
	print " Game Completed.\n"
print "Clearing the screen a final time and turning off the backlight..."
lcd.clear()
lcd.message("Goodbye!")
time.sleep(2)
lcd.backlight(lcd.OFF)
lcd.clear()
print " Done.\n"

print "Program End.\n"
