from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2
import pygame
import time
import sys
import keyboard

capture = ( 1200, 720 )
downscale = ( 1200 // 6, 720 // 6 )
upscale_window = False


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

	new_time = time.clock()

	deltaTime = new_time - timers[ name ]
	if reset: timers[ name ] = new_time

	return deltaTime

pygame.init()
screen = pygame.display.set_mode( capture if upscale_window else downscale )



while True:

	img = ImageGrab.grab( bbox = ( 0, 0, capture[ 0 ], capture[ 1 ] ) )
	img_small = img.resize( capture if upscale_window else downscale, resample = Image.BILINEAR )
	img_array = np.swapaxes( np.array( img ), 0, 1 )
	img_small_array = np.swapaxes( np.array( img_small ), 0, 1 )

	surf = pygame.display.get_surface()
	pygame.pixelcopy.array_to_surface( surf, img_array if upscale_window else img_small_array )

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()