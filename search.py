import cv2
import numpy as np
import check
from PIL import Image

correct = check.createArray( "images/search1.png" )
image = check.createArray( "images/search2.png" )
# draw = check.createArray( "images/blank.png" )

for xx in range( 80 ):
	for yy in range( 80 ):
		if check.checkPixel( correct[ 0, 0 ], image[ xx, yy ], 60 ):
			img_buffer = cv2.

# draw[ xx, yy ] = ( 0, 0, 0 )

# img = Image.fromarray( np.swapaxes( draw, 0, 1 ), 'RGB' )
# img.show()