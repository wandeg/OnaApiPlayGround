import requests
import functools

BASE_URL = "https://ona.io/api/v1/"

PROFILES_EP="https://ona.io/api/v1/profiles"

def fetchData(url):
	# success=False
	data={}
	resp=requests.get(url)
	success=resp.status_code=200
	if success:
		data=resp.json()
	return [success,data]

def fetchProfileData():
	success, profiles = fetchData(PROFILES_EP)
	if success:
		return profiles

def extract_attr(prof,attr):
	if prof.has_key(attr):
		return prof[attr]

def count_freqs(lst):
	freq_dct={}
	for item in lst:
		freq_dct[item]=freq_dct.get(item,1)+1

	return freq_dct


def main():
	prof=fetchProfileData()
	countries_alpha2=map(functools.partial(extract_attr,attr='country'),
		filter(lambda  x:x['country'] != '', prof))
	freqs=count_freqs(countries_alpha2)
	countries_unique=set(countries_alpha2)

if __name__ == '__main__':
	main()