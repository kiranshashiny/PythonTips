# PythonTips

##### Pretty Print

		import json
		
		# Pretty Print
		print json.dumps({'4': 5, '6': 7}, sort_keys=True,
		                  indent=4, separators=(',', ': '))
		{
		    "4": 5,
		    "6": 7
		}

#####  Adding data to a payload object.
		
		
		data = {}
		data['shashi'] = 'kiran'
		data['santosh'] = 'kris'
		
		json_data = json.dumps(data)
		print json_data
		
		### Pretty Print of the same data above.
		print json.dumps ( json_data, sort_keys=True, indent=4, separators=(',', ': '))
