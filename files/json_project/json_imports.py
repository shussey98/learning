
#json files - java script object notation
#json is a string
#must use double quotations

import json

file = open('friends_json.txt','r')
file_contents = json.load(file) # reads file and turns it into a dictionary
file.close()
#print(file_contents['friends'][0])

#Creating a json file - list of dictionaries
cars = [
    {'make':'Ford','model':'Fiesta'},
    {'make':'Ford','model':'Focus'}
]

file = open('cars_json.txt','w')
json.dump(cars,file)
file.close()

#json.load - reads file and turns to dict
#json.dump - writes json list of dicts to file
#json.loads - turns json str into list of dicts
#json.dumps - turns py list of dicts to json list of dicts

my_json_string = '[{"name":"Alfa Romeo", "released":1950}]'
print(json.dumps(cars))
incorrect_car = json.loads(my_json_string)
print(incorrect_car)