#------------------------------------------------------------------------------
# This module uses API from http://www.smszone.in. To use any other API, update
# the configuration file.
#------------------------------------------------------------------------------

import requests
import json
import os

#------------------------------------------------------------------------------
# Look for words 'to' and 'saying' to extract the receiver and message respect-
# ively. Example 'Send SMS to Rahul saying Hello World'
#------------------------------------------------------------------------------
def process_query(query):
	to        = None
	message   = None
	temp_list = query.split()

	for i in range(len(temp_list)):
		if temp_list[i]=='to':
			to = temp_list[i+1]
		elif temp_list[i]=='saying':
			message = temp_list[i+1:]

	return to, " ".join(message)


def run(query):
	dir_path = os.path.dirname(os.path.realpath(__file__))
	
	with open(os.path.join(dir_path, 'configurations/config.txt')) as data_file:    
	    json_obj = json.load(data_file)

	try:
		to, message = process_query(query)

		username = json_obj['sms']['username']
		password = json_obj['sms']['password']
		endpoint = json_obj['sms']['endpoint']
		receiver = json_obj['contacts'][to]

		endpoint = endpoint.replace('YOUR_USERNAME', username)
		endpoint = endpoint.replace('YOUR_PASSWORD', password)
		endpoint = endpoint.replace('YOUR_RECEIVER', receiver)
		endpoint = endpoint.replace('YOUR_MESSAGE', message + ' - from Automata')

		requests.get(endpoint)

	except:
		print 'Something went wrong in \'mod_sms\' module'

run('send sms to me saying Hello World')