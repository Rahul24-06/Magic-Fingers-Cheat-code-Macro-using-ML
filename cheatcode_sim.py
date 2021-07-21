import serial
import time
import keyboard

s = serial.Serial('COM128')  #Choose the COM Port
while True:	
	res = s.read()
	print(res)
	if res == "circle": #action
		keyboard.write('aspirin') #Type the Cheatcode
	if res == "double tap": #action
		keyboard.write('comeflywithme') #Type the Cheatcode
	if res == "square": #action
		keyboard.write('leavemealone') #Type the Cheatcode
	if res == "triangle": #action
		keyboard.write('thugtools') #Type the Cheatcode
		
	
