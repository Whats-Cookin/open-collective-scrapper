import csv
import json
from typing import Any

def pipeline(expense:Any) -> Any:
    pass
        
def return_query(slug: str,limit: int) -> Any:
    query = f"""
    {{
      expenses(account: {{ slug: "{slug}" }}, limit: {limit}) {{
        nodes {{
          id
          legacyId
          description
          longDescription
          amount
          accountCurrencyFxRate
          createdAt
        }}
      }}
    }}
    """
    return query

def create_csv_header():
    with open('result_response_dict.json', 'r') as json_file:
      data = json.load(json_file)
    output = data['data']['expenses']['nodes']
    with open('data_file.csv', 'a', newline='') as data_file: 
      csv_writer = csv.writer(data_file)
      header = list(output[0].keys())
      header.insert(0, "org_slug")
      csv_writer.writerow(header)

def to_csv(org_slug, result):
    output = result['data']['expenses']['nodes']
    with open('data_file.csv', 'a', newline='') as data_file: 
      csv_writer = csv.writer(data_file)
      for expense in output:
          value = list(expense.values()) 
          value.insert(0, org_slug)
          csv_writer.writerow(value)