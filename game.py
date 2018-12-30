import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

resetButton = 4
greenButton = 19
redButton = 17
blueButton = 27
yellowButton = 22
whiteButton = 13


greenLed = 21
redLed = 20
blueLed = 16
yellowLed = 12
whiteLed = 26

GPIO.setup(resetButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(greenButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(redButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(blueButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(yellowButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(whiteButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(blueLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(whiteLed, GPIO.OUT)

finish = False 
greenWin = False
redWin = False
blueWin = False
yellowWin = False
whiteWin = False
reset = False

while True:
		
	while (finish == False):

		greenButtonPressed = GPIO.input(greenButton)
		redButtonPressed = GPIO.input(redButton)
		blueButtonPressed = GPIO.input(blueButton)
		yellowButtonPressed = GPIO.input(yellowButton)
		whiteButtonPressed = GPIO.input(whiteButton)	
			
		if greenButtonPressed == True:
			print("greenButton pressed")
			finish = True
			greenWin = True
		elif redButtonPressed == True:
			print("redButton pressed")
			finish = True	
			redWin = True
		elif blueButtonPressed == True:
			print("blueButton pressed")
			finish = True	
			blueWin = True
		elif yellowButtonPressed == True:
			print("yellowButton pressed")
			finish = True		
			yellowWin = True
		elif whiteButtonPressed == True:
			print("whiteButton pressed")
			finish = True	
			whiteWin = True
		else:
			finish = False
		
		GPIO.output(greenLed, greenWin)
		GPIO.output(redLed, redWin)
		GPIO.output(blueLed, blueWin)
		GPIO.output(yellowLed, yellowWin)
		GPIO.output(whiteLed, whiteWin)	
		
	resetButtonPressed = GPIO.input(resetButton)
	if resetButtonPressed == True:
		print("resetButton pressed")
		GPIO.output(greenLed, False)
		GPIO.output(redLed, False)
		GPIO.output(blueLed, False)
		GPIO.output(yellowLed, False)
		GPIO.output(whiteLed, False)
		finish = False
		greenWin = False
		redWin = False
		blueWin = False
		yellowWin = False
		whiteWin = False	
    
GPIO.cleanup()
