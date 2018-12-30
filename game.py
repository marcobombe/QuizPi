import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# Buttons positions
resetButton 	= 	4
greenButton 	= 	19
redButton		= 	17
blueButton		= 	27
yellowButton 	= 	22
whiteButton 	= 	13

# Leds positions
greenLed 	= 	21
redLed 		= 	20
blueLed		= 	16
yellowLed 	= 	12
whiteLed 	= 	26

# Inputs declaration
GPIO.setup(resetButton, 	GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(greenButton, 	GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(redButton, 		GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(blueButton, 		GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(yellowButton, 	GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(whiteButton, 	GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Output declarations
GPIO.setup(greenLed, 	GPIO.OUT)
GPIO.setup(redLed, 		GPIO.OUT)
GPIO.setup(blueLed, 	GPIO.OUT)
GPIO.setup(yellowLed,	GPIO.OUT)
GPIO.setup(whiteLed, 	GPIO.OUT)

# Global variables
finish 		= False 

greenWin 	= False
redWin 		= False
blueWin 	= False
yellowWin	= False
whiteWin 	= False

# Strict polling
while True:
	
	# First button pressed identification
	while (finish == False):

		greenButtonPressed 	= 	GPIO.input(greenButton)
		redButtonPressed 	= 	GPIO.input(redButton)
		blueButtonPressed 	= 	GPIO.input(blueButton)
		yellowButtonPressed 	= 	GPIO.input(yellowButton)
		whiteButtonPressed 	= 	GPIO.input(whiteButton)	
			
		if greenButtonPressed == True:
			print("GREEN WIN")
			finish = True
			greenWin = True
		elif redButtonPressed == True:
			print("RED WIN")
			finish = True	
			redWin = True
		elif blueButtonPressed == True:
			print("BLUE WIN")
			finish = True	
			blueWin = True
		elif yellowButtonPressed == True:
			print("YELLOW WIN")
			finish = True		
			yellowWin = True
		elif whiteButtonPressed == True:
			print("WHITE WIN")
			finish = True	
			whiteWin = True
		else:
			finish = False
		
		# Light up winner color led
		GPIO.output(greenLed, greenWin)
		GPIO.output(redLed, redWin)
		GPIO.output(blueLed, blueWin)
		GPIO.output(yellowLed, yellowWin)
		GPIO.output(whiteLed, whiteWin)	
		
	# Reset for next round	
	resetButtonPressed = GPIO.input(resetButton)
	if resetButtonPressed == True:
		print("LED RESET")
		GPIO.output(greenLed, 	False)
		GPIO.output(redLed, 	False)
		GPIO.output(blueLed, 	False)
		GPIO.output(yellowLed, 	False)
		GPIO.output(whiteLed, 	False)
		finish 		= False
		greenWin 	= False
		redWin 		= False
		blueWin 	= False
		yellowWin 	= False
		whiteWin 	= False	
    
GPIO.cleanup()
