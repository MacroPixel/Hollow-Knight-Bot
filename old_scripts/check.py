import cv2
import numpy as np

def createArray( filepath ):

	return np.swapaxes( cv2.cvtColor( np.array( cv2.imread( filepath ) ), cv2.COLOR_BGR2RGB ), 0, 1 )

def checkPixel( px1, px2, thresh2 ):

	if not any( px1 ): return True

	for i in range( 3 ):
		if abs( int( px1[ i ] ) - int( px2[ i ] ) ) > thresh2: return False

	return True

def checkImage( template, comp, thresh1 = .05, thresh2 = 40, print_errors = False ):

	error = 0

	for xx in range( comp.shape[0] ):
		for yy in range( comp.shape[1] ):
			if not checkPixel( template[ xx, yy ], comp[ xx, yy ], thresh2 ): error += 1

	if print_errors: print( f"{ error } errors detected." )
	return ( ( error / ( template.shape[0] * template.shape[1] ) ) <= thresh1 )

def copyArray( array, start, size ):

	buffer = np.zeros( ( size[0], size[1], 3 ), dtype = int )

	for xx in range( size[0] ):
		for yy in range( size[1] ):
			buffer[ xx, yy ] = array[ start[0] + xx, start[1] + yy ]

	return buffer