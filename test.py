import search
import check

template_small = check.createArray( "images/search1.png" )
template = check.createArray( "images/search2.png" )
image = check.createArray( "images/search3.png" )
offset = ( 47, 66 ) 

search.findImage( template_small, template, image, offset )