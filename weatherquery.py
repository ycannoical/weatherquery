import requests 
import sys 	
import json
import re

print ("Time to get air temperature data!")
val = input("Enter date value(YYYY-MM-DD) to get air temperature data: ") 
regex = r"([0-9]{4}-[0-9]{2}-[0-9]{2})"
while len(re.findall(regex, val)) != 1:
	print ("Input value in wrong format. Format expected (YYYY-MM-DD). E.g. 2021-04-10")
	val = input("Enter date value(YYYY-MM-DD) to get air temperature data: ") 

target= "https://api.data.gov.sg/v1/environment/air-temperature?date=%s" % val  
r = requests.get(target)			
temperature_dict = json.loads(r.text)

if "invalid date format" in r.text or bool(temperature_dict) == False:
	print ("Something has gone wrong with the input or api. Contact your administrator")
	exit()

if bool(temperature_dict) == True :

	data = temperature_dict["metadata"]
	stations = data["stations"]

	print ("Selection a location from the list below"+"\n")
	for place in stations:
		print (place["name"])

	locationval = input("Enter one of the location above: ")
	stationid = ""
	id_dict = [place for place in stations if place["name"] == locationval]

	while len(id_dict) == 0:
		print ("Invaild Location. Input is case-sensitive"+"\n")
		locationval = input("Enter one of the location: ")
		id_dict = [place for place in stations if place["name"] == locationval]

	for val2 in id_dict:
		stationid = val2["id"] 

	items = temperature_dict["items"]
	for x in items:
		for y in (x["readings"]):
			final_temperature = [y for y in x["readings"] if y["station_id"] == stationid]
	for z in final_temperature:
		print ("The temperature is : "+str(z["value"]))
		

