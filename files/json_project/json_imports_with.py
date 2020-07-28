
import json
##CONTEXT MANAGERS
# with - as opens and closes file


with open('friends_json.txt','r') as file:
    file_contents = json.load(file) # reads file and turns it into a dictionary

#print(file_contents['friends'][0])

#Creating a json file - list of dictionaries
cars = [
    {'make':'Ford','model':'Fiesta'},
    {'make':'Ford','model':'Focus'}
]

with open('cars_json.txt','w') as file:
    json.dump(cars,file)

#json.load - reads file and turns to dict
#json.dump - writes json list of dicts to file
#json.loads - turns json str into list of dicts
#json.dumps - turns py list of dicts to json list of dicts

my_json_string = '[{"name":"Alfa Romeo", "released":1950}]'
print(json.dumps(cars))
incorrect_car = json.loads(my_json_string)
print(incorrect_car)

