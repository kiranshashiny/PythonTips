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

##### Pretty Print some big data ( a sample is listed here ) I want to proper format it
        

        '{"data": [{"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-14T06:49:20Z", "interval": 1, "enabled": false, "action": "info", "tagName": "USERAGENT", "longName": "Failed 404 messages", "threshold": 2, "id": "578735f02e266a62a3f3bc0d"}, {"createdBy": "vinayraj@in.ibm.com", "created": "2016-07-14T07:58:01Z", "interval": 1, "enabled": false, "action": "flagged", "tagName": "TRAVERSAL", "longName": "HTTP 4XX Errors", "threshold": 2, "id": "578746093c2b61552dbf3351"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:35:40Z", "interval": 1, "enabled": false, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "57905f2c3c2b61364c610e28"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:37:52Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "57905fb02e266a434f939b30"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:42:18Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "579060ba2e266a434f939cc9"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:43:39Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "5790610b2e266a434f939d5c"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:44:21Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "579061352e266a434f939da0"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:46:02Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "5790619a2e266a434f939e38"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:50:28Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "579062a43c2b6167fdb69b76"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:51:12Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "579062d03c2b6167fdb69bc5"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:51:55Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "579062fb3c2b6167fdb69c07"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:53:40Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "579063643c2b6167fdb69ca6"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:54:35Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "5790639b2e266a74f6e5ae57"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:57:03Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "5790642f2e266a74f6e5af3c"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:57:48Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "5790645c2e266a74f6e5af7f"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T05:59:22Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestSQLI", "threshold": 10, "id": "579064ba3c2b6167fdb69ec4"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T06:08:47Z", "interval": 1, "enabled": false, "action": "info", "tagName": "USERAGENT", "longName": "Increase in failed logins", "threshold": 2, "id": "579066ef3c2b6167fdb6a257"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T06:12:30Z", "interval": 1, "enabled": false, "action": "info", "tagName": "TRAVERSAL", "longName": "CheckDIrTraversal", "threshold": 1, "id": "579067ce3c2b6167fdb6a3ac"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T06:19:45Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579069813c2b6167fdb6a654"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T06:22:25Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "57906a212e266a74f6e5b87f"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T06:24:48Z", "interval": 1, "enabled": false, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "57906ab03c2b6167fdb6a830"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T06:28:31Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "57906b8f2e266a74f6e5babc"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-21T10:35:24Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "5790a56c2e266a74f6e61d3a"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-29T10:12:54Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579b2c263c2b61363289846c"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-29T10:21:58Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579b2e462e266a4518e9b7c6"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-29T10:28:32Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579b2fd03c2b613632898984"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-29T10:29:06Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579b2ff22e266a4518e9ba56"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-29T10:42:30Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579b33163c2b613632898dcc"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-29T10:48:33Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579b34812e266a4518e9c07f"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-29T10:50:15Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579b34e73c2b613632899066"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-29T10:57:55Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579b36b32e266a4518e9c339"}, {"createdBy": "shkiran4@in.ibm.com", "created": "2016-07-29T10:59:25Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "579b370d2e266a4518e9c3a8"}, {"createdBy": "vinayraj@in.ibm.com", "created": "2016-08-17T11:05:33Z", "interval": 10, "enabled": true, "action": "info", "tagName": "TRAVERSAL", "longName": "Repeated Failed Logins", "threshold": 3, "id": "57b444fd2e266a787204cd36"}, {"createdBy": "kiranshashiny+apiuser@gmail.com", "created": "2016-08-18T08:43:04Z", "interval": 1, "enabled": true, "action": "flagged", "tagName": "SQLI", "longName": "TestCustomAlert", "threshold": 20, "id": "57b575183c2b617ebcfdef64"}]}'

#####    To Pretty print it :
        import json
        import pprint
        dataX = json.loads ( corps.text )
        
        pprint.pprint(json.dumps(dataX));
        print json.dumps ( dataX, sort_keys=True, indent=4, separators=(',', ': '))


        {
    "data": [
        {
            "action": "info",
            "created": "2016-07-14T06:49:20Z",
            "createdBy": "shkiran4@in.ibm.com",
            "enabled": false,
            "id": "578735f02e266a62a3f3bc0d",
            "interval": 1,
            "longName": "Failed 404 messages",
            "tagName": "USERAGENT",
            "threshold": 2
        },
        {
            "action": "flagged",
            "created": "2016-07-14T07:58:01Z",
            "createdBy": "vinayraj@in.ibm.com",
            "enabled": false,
            "id": "578746093c2b61552dbf3351",
            "interval": 1,
            "longName": "HTTP 4XX Errors",
            "tagName": "TRAVERSAL",
            "threshold": 2
        },
        {.....



#####  Adding data to a payload object.
		
		
		data = {}
		data['shashi'] = 'kiran'
		data['santosh'] = 'kris'
		
		json_data = json.dumps(data)
		print json_data
		
		### Pretty Print of the same data above.
		print json.dumps ( json_data, sort_keys=True, indent=4, separators=(',', ': '))

![alt tag](https://cloud.githubusercontent.com/assets/14288989/16335968/6ba6fb62-3a27-11e6-80b0-d7998a2ecd7a.png)


##### Visual Recognition API




        with open(join(dirname(__file__), 'indianprez.jpg'), 'rb') as image_file:
            print(json.dumps(visual_recognition.detect_faces(images_file=image_file), indent=2))


		{
		  "images": [
		    {
		      "image": "indianprez.jpg", 
		      "faces": [
		        {
		          "gender": {
		            "gender": "MALE", 
		            "score": 0.817574
		          }, 
		          "age": {
		            "max": 44, 
		            "score": 0.384491, 
		            "min": 35
		          }, 
		          "face_location": {
		            "width": 216, 
		            "top": 160, 
		            "left": 144, 
		            "height": 242
		          }
		        }
		      ]
		    }
		  ], 
		  "images_processed": 1
		}


Code:
	import json
	from pprint import pprint
	
	with open('data.json') as data_file:    
	    data = json.load(data_file)
	
	pprint(data)
	
	print "name of the image "
	print data['images'][0]['image']
	
	print "printing faces"
	print data['images'][0]['faces']
	
	print "printing face_location"
	print data['images'][0]['faces'][0]['face_location']
	
	print "print face_location width"
	print data['images'][0]['faces'][0]['face_location']['width']


Output:

		name of the image 
		indianprez.jpg

		printing faces
		[{u'gender': {u'gender': u'MALE', u'score': 0.817574}, u'age': {u'max': 44, u'score': 0.384491, u'min': 35}, u'face_location': {u'width': 216, u'top': 160, u'height': 242, u'left': 144}}]

		printing face_location
		{u'width': 216, u'top': 160, u'height': 242, u'left': 144}

		print face_location width
		216
		
