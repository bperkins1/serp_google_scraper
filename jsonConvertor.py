import json
import pandas
import openpyxl
import csv
import pprint
import validators
from email_scraper import get_email

def json_to_csv(places_info, file_name, emails=True):
    all_rows = []
    header = ["Name", "Address", "Phone number", "Website", "Hours"]
    if emails == True:
        header.append("Email")

    for lis in places_info:
        for place in lis:
            num = 0
            row_num = []
            
            row_num.extend((place.get("title"),place.get("address"),place.get("phone"),place.get("website"),place.get("hours")))
            
            # get email from "website" attribute url
            if emails == True:
                email_url = str(place.get("website"))
                if validators.url(email_url) == True:
                    emails = get_email(email_url)
                    row_num.append(emails)
                    
                else:
                    row_num.append("invalid url")

            all_rows.append(row_num)
            num += 1


    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        # write the data
        for row in all_rows:
            writer.writerow(row)

#takes api response and saves a file to json. Returns the Json
def results_to_json(results):
    with open("data_file.json", "w") as write_file:
        json.dump(results, write_file)


#takes json file and returns python collection
def load_json(json_file):
    with open(json_file, "r") as read_file:
        obj = json.load(read_file)
    
        return obj
