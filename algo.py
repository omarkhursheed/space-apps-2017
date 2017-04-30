# All are coming live in real time.
rainfall_amount = ''
ground_water = ''
proximity_to_water_body = ''
history = {}
livedata = ('', '')

slope = True
loose_soil = True
threshold_calamity = 0.60

def near(a, b):
	"""
	Checks whether or not the coordinates given: a and b are near to each other
	If yes, returns the coordinates of a.
	If no, returns -1.
	"""
	pass


def get_latest(previous_entries):
	"""
	fetch from { dict(year) --> (x, y, z) } the latest (sorted by year). 
	"""
	pass

def calulate_threshold(history, livedata, x):
	"""
	:param:`history` dict(lat, long) --> { dict(year) --> (x, y, z) }  at that lat, long, year.
	:param:`livedata` tuple current (lat, long)
	:param:`x` the property amongst x, y, z.

	:return: dict((lat, long), x) --> threshold of x at lat, long.
	"""
	threshold_values = {}
	# near returns latt, long pair which is present in the history
	coordinates = near(history.keys()[:-1], livedata)
	if coordinates != -1:
		previous_entries = history.get(coordinates)
		latest_entry = get_latest(previous_entries)
		threshold_values[livedata, x] = latest_entry
	return threshold_values


def degree_of_belonging():
	rainfall_threshold = threshold_values(history, rainfall_amount)
	gw_threshold = threshold_values(history, ground_water)
	prox_threshold = threshold_values(history, proximity_to_water_body)
	set_rainfall = t_divide(rainfall_amount, rainfall_threshold)
	set_gw = t_divide(rainfall_amount, ground_water)
	set_prox = t_divide(rainfall_amount, prox_threshold)
	(weight_rain, weight_gw, weight_prox) = (1, 1, 1)  # Let's say for now, we can train afterwards
	degree = (weight_rain * set_rainfall,
			  weight_gw * set_gw ,
			  weight_prox * set_prox)
	return degree

def main():
	"""
	I assume we have history, livedata coming.	
	"""
	# They should be bool for now, we can take their factor into account afterwards
	if slope and loose_soil:
		degree = degree_of_belonging()
	if degree > threshold_calamity:
		print("I am in danger")




















