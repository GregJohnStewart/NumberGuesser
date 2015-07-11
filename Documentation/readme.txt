numberGuesser V1.0 ReadMe

Author: Greg Stewart
Copyright 2014 Greg Stewart

For more information on this project and more, visit:

http://www.gjstewart.net/projects/


	Meant as a simple program that tries to guess a number that the user keeps
in his/ her head. Reverse of the "numGuess" game 
(gjstewart.com/projects/numGuess_proj.html). Made for use with the Raspberry Pi
and its 16x2 Character LCD Display.
	
It uses a relatively simple algorithm to guess numbers:

Data used:
-Lower bounds of number (starting at 0)
	-the highest number it knows that is less than the target
-Upper bounds of number (starting at 10)
	-the lowest number it knows that is higher than the target
	
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
		
		
		
DIRECTIONS: (assuming you have unzipped the files and have python
				 2.7.6 installed)

Only for use on the Raspberry Pi with a connected 16x2 Character LCD Display
	 by Adafruit Industries.
	 https://www.adafruit.com/products/1110


1) Get to a terminal window, if using the GUI


2) Navigate to the folder where the numGuess.py file is kept


3) Execute the code
	
	Bash Script command: sudo python numberGuesser.py
	
NOTE:

	> You may need to restart the script until it displays correctly. My LCD 
		display sometimes displays garbage until you restart the script.
