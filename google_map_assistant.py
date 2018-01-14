import urllib.request
import json

# default settings
direction_url = 'https://maps.googleapis.com/maps/api/directions/json?'
distance_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
# choose only one keys respect to the above url
api_key_direction = 'AIzaSyDVGTc3eA3wAsOvDLE7b9a9anKGM9Bbqw4'
api_key_distance = 'AIzaSyBAsN8SOpjIClACNVkg5pi-vSM4C17mAek'
# location settings
units = 'metric'
origin = 'Jln Mutiara Emas 9/23, Taman Mount Austin, 81100 Johor Bahru, Johor, Malaysia'.replace(' ', '+')
destination = 'Singapore Chinese Cultural Centre 1 Straits Boulevard, Singapore, Singapore 018906'.replace(' ', '+')
nav_request = 'units={}&origins={}&destinations={}&key={}'.format(units,
                                                                  origin,
                                                                  destination,
                                                                  api_key_distance)
# getting url request and response back in json
request = distance_url + nav_request
response = urllib.request.urlopen(request).read()  # return in string
returned_json = json.loads(response)
elements = returned_json['rows'][0]['elements'][0]
print('Full Json: ', returned_json)
# if the returned status is ok, then only it prints out all details
if returned_json['status'] == 'OK':
    print('From: ', returned_json['destination_addresses'][0])
    print('To: ', returned_json['origin_addresses'][0])
    print('Distance: ', elements['distance']['text'])
    print('Duration: ', elements['duration']['text'])
else:
    print('Invalid Api keys')


