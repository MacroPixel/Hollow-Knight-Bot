import check
import numpy as np

image = check.createArray( "images/steam2.png" )
copy = check.copyArray( image, ( 20, 20 ), ( 3, 3 ) )

print( image[ 23, 20 ] )
print( copy[ 0, 1 ] )