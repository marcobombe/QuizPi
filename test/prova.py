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


GPIO.output(greenLed, False)
GPIO.output(redLed, False)

while True:

	resetButtonPressed = GPIO.input(resetButton)
	greenButtonPressed = GPIO.input(greenButton)
	redButtonPressed = GPIO.input(redButton)
	blueButtonPressed = GPIO.input(blueButton)
	yellowButtonPressed = GPIO.input(yellowButton)
	whiteButtonPressed = GPIO.input(whiteButton)
	
	if resetButtonPressed == True:
		print("resetButton pressed")
		blink = False
	elif greenButtonPressed == True:
		print("greenButton pressed")
		blink = False
	elif redButtonPressed == True:
		print("redButton pressed")
		blink = False	
	elif blueButtonPressed == True:
		print("blueButton pressed")
		blink = False	
	elif yellowButtonPressed == True:
		print("yellowButton pressed")
		blink = False	
	elif whiteButtonPressed == True:
		print("whiteButton pressed")
		blink = False			
	else:
		blink = True

	if blink == True:
		GPIO.output(greenLed, True)
		GPIO.output(redLed, True)
		GPIO.output(blueLed, True)
		GPIO.output(yellowLed, True)
		GPIO.output(whiteLed, True)
		sleep(0.05)
		GPIO.output(greenLed, False)
		GPIO.output(redLed, False)
		GPIO.output(blueLed, False)
		GPIO.output(yellowLed, False)
		GPIO.output(whiteLed, False)
		sleep(0.05)
    
GPIO.cleanup()
