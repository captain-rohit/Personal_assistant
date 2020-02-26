import os, requests, json, speech_recognition 


POST_COMMAND_URL = "http://localhost:5000/decode_command"
POST_MODULE_URL  = "http://localhost:5000/execute_func"

while True:
	recogniser_obj = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as source:
		print "Query : ",
		audio = recogniser_obj.listen(source)

	try:
		input_query = recogniser_obj.recognize_google(audio)
		print input_query

		headers     = {"Content-type": "application/json"}

		data        = json.dumps({"command":input_query})
		request_obj = requests.post(POST_COMMAND_URL, data=data, headers=headers)

		data        = json.dumps({"module":request_obj.text,"data":input_query})
		request_obj = requests.post(POST_MODULE_URL, data=data, headers=headers)

	except:
		print "Nothing detected"