
import requests
import json
import urllib.parse as urlparse
from urllib.parse import urlencode


# takes a serpapi response and the amount of pages you want to scrape
# returns a list of lists of places and their information
def get_place_info(MapsSearchObject, pages, params):
	places = []
	current = []

	
	for num in range(pages):

		if len(places) == 0:
			# appears to be get dict for GoogleSearch and json for archived b
			results = MapsSearchObject.get_dict()

			current.append(results.get('serpapi_pagination').get('current'))

			print("requested original search")

		else:
			results = requests.get(new_url, timeout=60000).json()

			print("using new url")

			if results.get('serpapi_pagination').get('current') in current:
				break

			current.append(results.get('serpapi_pagination').get('current'))


		if "error" in results:
			print(f"error: " + results["error"])
			break

		# collect the data
		page_places = results.get("local_results")
		places.append(page_places)
		print("added places")


		url = results.get("serpapi_pagination").get("next")
		
		#make url work for another api request
		# if geopy breaks, get coords from first result and insert here
		url_parse = urlparse.urlparse(url)
		query = url_parse.query
		url_dict = dict(urlparse.parse_qsl(query))
		url_dict.update(params)
		url_new_query = urlparse.urlencode(url_dict)
		url_parse = url_parse._replace(query=url_new_query)
		new_url = urlparse.urlunparse(url_parse)
		print(new_url)



	return places

# grab query from serpapi archive
def get_archived(search_id, api_key):
	url = f"https://serpapi.com/searches/{search_id}.json?api_key={api_key}"
	return requests.get(url)

# early way to save search ids - just use serpapi website
def save_search(GoogleSearchObject, name):
	results = GoogleSearchObject.get_dict()
	search_id = results.get("search_metadata").get("id")
	query = results.get("search_parameters").get("q")
	location_query = results.get("search_parameters").get("location_requested") 
	with open('searchIds.py', 'w') as f:
		f.write(f'id_{name} = \"{search_id}\"\n')
		f.write(f'query_{name} = \"{query}{location_query}\"\n')
	return search_id



# multi threading is an option to perform many concurrent searches
# , see https://github.com/serpapi/google-search-results-python