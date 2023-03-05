import requests
import json

def isSold(product: dict) -> bool:
    if product["metadata"]["store"] == "poshmark":
        r = requests.get('https://poshmark.com/vm-rest/posts/' + product['productID']).json()
        sold_string = r['inventory']['status']
        return sold_string == 'sold_out'
    

#testing
#with open('test.json') as user_file:
#  file_contents = user_file.read()
#  parsed_json = json.loads(file_contents)
#  print(isSold(parsed_json))