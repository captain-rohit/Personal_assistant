#------------------------------------------------------------------------------
# This module uses API from Wolframalpha and TextRzor. To use any other API,
# update the configuration file.
#------------------------------------------------------------------------------

import os
import json
import wolframalpha
import textrazor


def run(query):

	dir_path = os.path.dirname(os.path.realpath(__file__))
	
	with open(os.path.join(dir_path, 'configurations/config.txt')) as data_file:    
	    json_obj = json.load(data_file)

	# Initialize the API keys
	wclient           = wolframalpha.Client(json_obj['wolframalpha'])
	textrazor.api_key = json_obj['textrazor']
	
	# Extract the true meaning of the sentence
	tclient  = textrazor.TextRazor(extractors=["entities"])
	response = tclient.analyze(query)
	query    = response.entities()[0].id

	# Perform query
	response = wclient.query(query)

	for pod in response.pods:

		if pod.title=='Wikipedia summary' and pod.text != None:
			print 'Wikipedia summary : ' + pod.text

		if pod.title=='Response':
			print pod.text

		if pod.title=='Basic information':
			print pod.text.split('\n')[0] + '\n' + pod.text.split('\n')[1]

		if pod.title=='Result' or pod.title=='Current result' or pod.title=='Approximate result' or pod.title=='Results' or pod.title=='Average result':
			print pod.text

		if pod.title=='Notable facts':
			print '* ' + pod.text.split('\n')[0] + '\n* ' + pod.text.split('\n')[1] + '\n* ' + pod.text.split('\n')[2]

		if pod.title=='Bordering countries/regions':
			print 'Bordering countries/regions -> ' + pod.text

		if pod.title=='Location':
			print pod.text

		if pod.title=='Capital city':
			print 'Capital city -> ' + pod.text
		
		if pod.title=='Currency':
			print 'Currency -> ' + pod.text.split('\n')[1]

		if pod.title=='Value':
			print pod.text.split('\n')[0]

		if pod.title=='Morse code translation':
			print pod.text