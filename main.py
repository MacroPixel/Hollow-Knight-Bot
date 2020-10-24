import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2
import pygame
import time
import sys
import keyboard
import location as loc


capture = ( 1200, 720 ) # normal window size
downscale = ( 1200 // 6, 720 // 6 ) # downscaled window size
upscale_window = False # determines which size to use

timers = {} # used for timing actions

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# adds to timers dictionary
def clockInit( name ):

    global timers

    timers[ name ] = time.clock()

# returns time
def clockCheck( name, reset = True ):

    global timers

    new_time = time.clock()

    deltaTime = new_time - timers[ name ]
    if reset: timers[ name ] = new_time

    return deltaTime

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# window
pygame.init()
screen = pygame.display.set_mode( capture if upscale_window else downscale )
pygame.display.set_caption( "Hollow Knight Bot" )

# MAIN LOOP
while True:

    # take screenshot/convert to different image types
    img = ImageGrab.grab( bbox = ( 0, 0, capture[ 0 ], capture[ 1 ] ) )
    img_small = img.resize( capture if upscale_window else downscale, resample = Image.BILINEAR )
    img_cv2 = cv2.cvtColor( np.uint8( img if upscale_window else img_small ), cv2.COLOR_BGR2GRAY )
    img_array = np.swapaxes( np.uint8( img ), 0, 1 )
    img_small_array = np.swapaxes( np.uint8( img_small ), 0, 1 )

    # generate corner outputs (determine where image is found)
    images = ( 'fk_template_1', 'fk_template_2' )
    cornerOutput = {}
    for image_name in images:
        cornerOutput[ image_name ] = ( loc.fromTemplate( img_cv2, cv2.imread( f'images/{ image_name }.png', 0 ), .9 ) )

    # setup surface
    surf = pygame.display.get_surface()
    pygame.pixelcopy.array_to_surface( surf, img_array if upscale_window else img_small_array )

    # determine corner coords of closest match
    # lowest matchvalue = closest match; cornerOutput[ name ][ 0 ] is matchvalue, ..[ 1 ] is ( cornerX, cornerY )
    min_value = 0.3
    min_key = "error"
    for image_name in cornerOutput:
        if cornerOutput[ image_name ][ 0 ] < min_value:
            min_value = cornerOutput[ image_name ][ 0 ]
            min_key = image_name
    corner1, corner2 = cornerOutput[ image_name ][ 1 ]
    print( min_key )

    # if a match is found, draw rectangle there
    if min_key != "error": pygame.draw.rect( surf, ( 0, 255, 0 ), pygame.Rect( corner1, ( corner2[0] - corner1[0], corner2[1] - corner1[1] ) ), 2 )

    # handle other pygame stuff
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()