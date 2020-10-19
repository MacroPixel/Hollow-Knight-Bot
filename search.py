import cv2
import numpy as np
import check
from PIL import Image

correct = check.createArray( "images/search1.png" )
image = check.createArray( "images/search2.png" )
# draw = check.createArray( "images/blank.png" )

check.createRef( "images/search1.png" )

for xx in range( image.shape[0] - correct.shape[0] ):
	for yy in range( image.shape[1] - correct.shape[1] ):
		if check.checkPixel( correct[ 0, 0 ], image[ xx, yy ], 60 ):

			buffer = check.copyArray( image, ( xx, yy ), ( correct.shape[0], correct.shape[1] ) )
			if check.checkImage( buffer, 0, zz50 ): print( f"{ xx }, { yy }" )

# draw[ xx, yy ] = ( 0, 0, 0 )

# img = Image.fromarray( np.swapaxes( draw, 0, 1 ), 'RGB' )
# img.show()