import cv2
import numpy as np

def createImage( filepath ):

	return np.swapaxes( cv2.cvtColor( np.array( cv2.imread( filepath ) ), cv2.COLOR_BGR2RGB ), 0, 1 )

def validatePixel( px1, px2, sensitivity ):

	if not any( px1 ): return True

	for i in range( 3 ):
		if abs( int( px1[ i ] ) - int( px2[ i ] ) ) > sensitivity: return False

	return True

def loadImage( filepath ):

	global template

	template = createImage( filepath )

def checkImage( filepath, thresh1 = 50, thresh2 = 40 ):

	comp = createImage( filepath )
	error = 0

	for xx in range( 50 ):
		for yy in range( 50 ):
			if not validatePixel( template[ xx, yy ], comp[ xx, yy ], thresh2 ): error += 1

	print( f"{ error } errors detected." )
	return ( error <= thresh1 )

loadImage( 'images/steam1.png' )
print( "These are similar images." if checkImage( 'images/steam5.png' ) else "These are not similar images." )