from google_search import get_place_info
from jsonConvertor import json_to_csv
from get_coordinates import get_coordinates
from serpapi import GoogleSearch
import config
from os.path import exists

if config.key = "YOUR_API_KEY_HERE":
  key = input("Enter your api key: ")
else:
  key = config.key
location_query = input("Location to search (city, state, and/or zip): ")
query = input("What places do you want to search for: ")
file_name = query[0:8]
number = int(input("How many results do you want? (enter a number) "))
if number > 1000:
  print("Can't search for that many results, reducing to 1000...")
  number = 1000
amount = number//20

coordinates = get_coordinates(location_query)
latitude = coordinates[0]
longitude = coordinates[1]



maps_params = {
  "engine": "google_maps",
  "q": f"{query}",
  "ll": f"@{latitude},{longitude},11z", #z for zoom.-can change for precision
  "hl": "en",
  "gl": "us",
  "type": "search",
  "api_key": key
}


search = GoogleSearch(maps_params)

place_results = get_place_info(search, amount, maps_params)

json_to_csv(place_results, f"data/{file_name}.csv")

if exists(f"data/{file_name}.csv"):
  print(f"information saved to 'data/{file_name}.csv'")