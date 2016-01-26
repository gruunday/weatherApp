from urllib2 import Request, urlopen, URLError
import sys

###################################
# manual controls for co-ordinates
# lat = str(sys.argv[1])
# lng = str(sys.argv[2])
###################################

responce_recived = False
found = False

###################################
# DCU Co-Ordintes for testing
# lat = str(53.385267)
# lng = str(-6.256889)
###################################

###################################
# sets arg to area to search
###################################
area = sys.argv[1:]
area = " ".join(area)


######################################################################################
# searchs for the coordinates for the place you have selected
# coordinates found at gael-varoquaux.info/blog/wp-content/uploads/2008/12/cities.txt
# 
######################################################################################
with open("cities.txt", "r") as f:
	for line in f.readlines():
		split_line = line.split("/")
		#print split_line
		if area.lower() == split_line[0].lower():
			lng = str(split_line[1])
			bad_newline = split_line[2]
			no_newline = bad_newline[0:len(bad_newline) - 1]
			lat = str(no_newline)
			found = True
			break
			

if found == True:	
	####################################
	# gets data from forecast.io api
	####################################
	url = "https://api.forecast.io/forecast/7cbf3f654ce70e2d412ba606a5de4bfb/" + lat + "," + lng + "?units=ca&exclude=daily,minutly,flags"
	request = Request(url)
else:
	print "Not found. Did you enter a city?"
	sys.exit()

try:
	responce = urlopen(request)
	data = responce.read()
	useful_data = data[0:500]
	current_data = useful_data.split(",")
	responce_recived = True
except URLError, e:
	print "No data. Got an error code.", e



def outputs():
	############
	# timezone #
	############
	timezone = current_data[2]
	last_position = int(len(timezone) - 1)
	print timezone[12:last_position]

	######################
	# summary of weather #
	######################
	weather = current_data[5]
	last_position = int(len(weather) - 1)
	print weather[11:last_position]

if responce_recived == True:
	outputs()
