#!/usr/bin/env python

import requests
import json
import datetime
import sys

# By default, function searches for all MARTA routes.
def getBuses(route=''):

	#Base URL for MARTA API
	base = 'http://developer.itsmarta.com/BRDRestService/RestBusRealTimeService/'

	# If user does not input a value for route number, use 'GetAllBus' API call
	if route == '':
		query = 'GetAllBus'

	# Else, use 'GetBusByRoute' API call with user-defined route number
	else:
		query = 'GetBusByRoute/' + str(route)

	# Formulate URL request and format response as json object
	url = base+query
	response = requests.get(url)
	buses = response.json()

	# Prints entirety of json response
	#print(buses)

	# For each bus in response, print a few pieces of data.
	lst = []
	for bus in buses:
		lst.append({'route':bus['ROUTE'],'lat':bus['LATITUDE'],'lon':bus['LONGITUDE'],'adher':bus['ADHERENCE'],'vehicle':bus['VEHICLE'],'msgtime':bus['MSGTIME']})
	lst.reverse()
	return lst

def main():

	# Input function to obtain route number from user
	route = raw_input('\n\nPlease enter a route number (leave blank for all routes):\n\n')

	# Call getBuses function with user-defined route number
	getBuses(route)

if __name__ == '__main__':
	main()
