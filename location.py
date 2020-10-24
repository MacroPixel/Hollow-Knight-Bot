import cv2
import numpy as np

# locate using template
def fromTemplate( img, template, thresh = 0.28 ):
    w, h = template.shape[ ::-1 ]

    res = cv2.matchTemplate( img, template, cv2.TM_SQDIFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )

    top_left = min_loc
    bottom_right = ( top_left[0] + w, top_left[1] + h )

    # min_val is strength of match
    return ( min_val, ( top_left, bottom_right ) )