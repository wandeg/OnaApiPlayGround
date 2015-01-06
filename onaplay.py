import requests
import functools

BASE_URL = "https://ona.io/api/v1/"

PROFILES_URL="https://ona.io/api/v1/profiles"

def fetchData(url):
	# success=False
	data={}
	resp=requests.get(url)
	success=resp.status_code==200
	if success:
		data=resp.json()
	return [success,data]


def fetch_profiles_with_attr(profile,attr):
	if profile.has_key(attr):
		return profile[attr]

def count_freqs(lst):
	freq_dct={}
	for item in lst:
		freq_dct[item]=freq_dct.get(item,1)+1

	return freq_dct


def main():
	success, profiles=fetchData(PROFILES_URL)
	countries_alpha2=map(functools.partial(fetch_profiles_with_attr,attr='country'),
		filter(lambda  x:x['country'] != '', profiles))
	freqs=count_freqs(countries_alpha2)
	countries_unique=set(countries_alpha2)

if __name__ == '__main__':
	main()