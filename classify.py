import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from pprint import pprint

test_url = 'https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg'

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='2ad1de1d6651cba0046f8b4d7056d6d9ae61f53e')

#with open(join(dirname(__file__), 'photo.jpg'), 'rb') as image_file:
#    print(json.dumps(visual_recognition.detect_faces(images_file=image_file), indent=2))

with open(join(dirname(__file__), 'photo.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(images_file=image_file), indent=2))


with open(join(dirname(__file__), 'photo.jpg'), 'rb') as image_file:
    data = json.dumps(visual_recognition.classify(images_file=image_file), indent=4, separators=(',',':'))
    #pprint(data)

#   print "name of the image "
#	print data['images'][0]['image']
#	print "printing faces"
#	print data['images'][0]['faces']
#	print "printing face_location"
#	print data['images'][0]['faces'][0]['face_location']
#	print "print face_location width"
#	print data['images'][0]['faces'][0]['face_location']['width']
