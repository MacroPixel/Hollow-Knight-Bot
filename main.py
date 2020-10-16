from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2
import pygame
import time
import sys
import keyboard

# def my_line( img, start, end ):
# 	thickness = 2
# 	line_type = 8

# 	cv2.line( img, start, end, ( 0, 0, 0 ), thickness, line_type )

timers = {}

def clockInit( name ):

	global timers

	timers[ name ] = time.clock()

def clockCheck( name, reset = True ):

	global timers

	newTime = time.clock()

	deltaTime = newTime - timers[ name ]
	if reset: timers[ name ] = newTime

	return deltaTime

pygame.init()
screen = pygame.display.set_mode( ( 1200 // 3, 720 // 3 ) )



while True:

	clockInit( 'a' )
	print( 'imggrab' )
	img = ImageGrab.grab( bbox = ( 0, 0, 1200, 720 ) )
	print( clockCheck( 'a' ) )
	print( 'resize' )
	img = img.resize( ( 1200 // 3, 720 // 3 ), resample = Image.NEAREST )
	print( clockCheck( 'a' ) )
	print( 'swapaxes' )
	img_array = np.swapaxes( np.array( img ), 0, 1 ) # this is the array obtained from conversion
	print( clockCheck( 'a' ) )
	print( 'convert color' )
	frame = cv2.cvtColor( img_array, cv2.COLOR_BGR2RGB )
	print( clockCheck( 'a' ) )

	print( 'get surface' )
	surf = pygame.display.get_surface()
	print( clockCheck( 'a' ) )
	print( 'array to surface' )
	pygame.pixelcopy.array_to_surface( surf, img_array )
	print( clockCheck( 'a' ) )

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()