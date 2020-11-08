import cv2
import numpy as np

# locate using template
def fromTemplate( img, template, thresh = 0.28 ):

    # normal orientation
    # tbh this is all copy and pasted
    w, h = template.shape[ ::-1 ]

    res = cv2.matchTemplate( img, template, cv2.TM_SQDIFF_NORMED )
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( res )

    # check reversed
    res_1 = cv2.matchTemplate( img, cv2.flip( template, 1 ), cv2.TM_SQDIFF_NORMED )
    min_val_1, max_val_1, min_loc_1, max_loc_1 = cv2.minMaxLoc( res_1 )
    if min_val_1 < min_val:
        res_1, min_val, max_val, min_loc, max_loc = res_1, min_val_1, max_val_1, min_loc_1, max_loc_1

    top_left = min_loc
    bottom_right = ( top_left[0] + w, top_left[1] + h )

    # min_val is strength of match
    return ( min_val, ( top_left, bottom_right ) )