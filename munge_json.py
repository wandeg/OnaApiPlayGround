import json
import requests
from onaplay import *

URL="http://api.worldbank.org/countries?format=json&per_page=262"
#data fetched from world bank API
success, data=fetchData(URL)

#data is a list of country dicts with various attributes
countries=filter(lambda x:x['capitalCity'] != '', data[1])
countries=filter(lambda x:x.has_key('iso2Code'), countries)
countries=filter(lambda x:x.has_key('longitude'), countries)
countries=filter(lambda x:x.has_key('latitude'), countries)
# with open('static/data/country-capitals.json') as f:
# 	count_cap_data = json.load(f)
# 	print type(count_cap_data)
# new_count = filter(lambda x: x['CountryCode'] != 'NULL' ,count_cap_data)
# print new_count[0]

with open('static/data/world_countries.json') as f:
	world_count_data = json.load(f)
	# Data from the world countries json file from udacity
	# print type(world_count_data)
print world_count_data.keys()

def edit_world_data(ccapdict,worlddict):
	'''Takes dict with countries and capital cities
	Extracts capital cities and mutates dict from udacity to 
	include the capital cities'''
	if ccapdict['id']==worlddict['id']:
		worlddict['CapitalLongitude']=ccapdict['longitude']
		worlddict['CapitalLatitude']=ccapdict['latitude']
		worlddict['alpha2'] =ccapdict['iso2Code']
	return worlddict
wds=[]
for c in countries:
	for w in world_count_data['features']:
		wds.append(edit_world_data(c,w))

# print wds[0].keys()