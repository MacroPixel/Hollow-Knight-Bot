import time

timers = {}

def clockInit( name ):

	global timers

	timers[ name ] = time.clock()

def clockCheck( name, reset = True ):

	global timers

	timePrev = timers[ name ]
	timers[ name ] = time.clock()

	result = timers[ name ] - timePrev
	return result

clockInit( "a" )
time.sleep( 2 )
print( clockCheck( "a" ) )
time.sleep( 2 )