import os
import json
import requests
from lib.pipe import return_query, create_csv_header, to_csv
from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv('TOKEN')

url = 'https://api.opencollective.com/graphql/v2'
headers = {'Content-Type': 'application/json', 'Personal-Token': TOKEN}

def fetch_result(query):
    payload = {'query': query}
    response = requests.post(url, headers=headers, json=payload)
    response_dict = json.loads(response.text)
    # print("fetch_result_response_dict" ,response_dict)
    with open("result_response_dict.json", "w") as file:
      json.dump(response_dict, file)

    return response_dict

def run_one(limit: int):
    org_slug = None 
    with open('org_file.txt', 'r') as file:
        content = file.readline()
        slug = content.strip()
        print("SLUG", slug)
        query = return_query(slug, limit)
        res = fetch_result(query)
        with open('result.json', 'r') as json_file:
          data = json.load(json_file)
          to_csv(org_slug=slug, result=data)
        org_slug = slug

    return org_slug

def run_many(limit: int):
  create_csv_header()
  with open('org_file.txt', 'r') as file:
      for slug in file:
        slug = slug.strip()
        print("Fetching", slug, 'data')
        query = return_query(slug, limit)
        res = fetch_result(query)
        with open('result.json', 'r') as json_file:
          data = json.load(json_file)
          to_csv(org_slug=slug, result=data)