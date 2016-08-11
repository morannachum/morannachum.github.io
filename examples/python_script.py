import requests
import argparse
import json
import datetime

# Writes to a JSON file.
# Input: filename/location string, data in the form of array of
#	dictionaries
###################################################################
def toJSON(filename, data):
	with open(filename, 'w') as outfile:
		json.dump(data, outfile)


# Call a given link.
# Input: API link to ping
###################################################################
def callAPI(link):
	response = requests.get(link)
	return response

# Parses incoming information
######################################################################
def commandLineSetup():
    commandParser = argparse.ArgumentParser(description="Pings an API link for data "
                                                         "and outputs data to JSON file")
    commandParser.add_argument("-l", "--link", help="API link to ping for information")
    commandParser.add_argument("-o", "--outputfile", help="Name/Path of the JSON output file")

    args = commandParser.parse_args()

    return args.link, args.outputfile


######################################################################
# MAIN 
######################################################################

def main():
	LINK, OUTPUT = commandLineSetup()

	# Check that proper inputs were provided
	if not LINK or not OUTPUT:
		print str(datetime.datetime.now()) + " - Insufficient inputs provided"
		exit()

	print str(datetime.datetime.now()) + " - Calling link %s" % LINK
	response = callAPI(LINK)
	print str(datetime.datetime.now()) + " - Outputting to file %s" % OUTPUT
	toJSON(OUTPUT, response.json())
	print str(datetime.datetime.now()) + " - Done!"

if __name__ == "__main__":
	main()
