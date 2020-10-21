import cv2
import numpy as np
import check
from PIL import Image

template_small = check.createArray( "images/search1.png" )
template = check.createArray( "images/search2.png" )
image = check.createArray( "images/search3.png" )
offset = ( 47, 66 ) 

def findImage( template_small, template, image, offset ):

	step = 5
	xx = 0

	while xx < ( image.shape[0] - template_small.shape[0] ):

		yy = 0

		while yy < ( image.shape[1] - template_small.shape[1] ):

			if check.checkPixel( template_small[ 0, 0 ], image[ xx, yy ], 60 ):

				buffer = check.copyArray( image, ( xx, yy ), ( template_small.shape[0], template_small.shape[1] ) )

				if check.checkImage( template_small, buffer, 0, 50 ):

					coords = ( xx - offset[0], yy - offset[1] )
					if check.checkImage( template, check.copyArray( image, coords, ( template.shape[0], template.shape[1] ) ) ):

						print( f"Similar found at coordinates ({ coords[0] }, { coords[1] })" )

			yy += step
		xx += step