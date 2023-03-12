import requests
import json

def isSold(product: dict) -> bool:
    if product["metadata"]["store"] == "poshmark":
        r = requests.get('https://poshmark.com/vm-rest/posts/' + product['productID']).json()
        if 'error' in r:
            return True
        sold_string = r['inventory']['status']
        return sold_string == 'sold_out'
    if product["metadata"]["store"] == "depop":
        r = requests.get('https://webapi.depop.com/api/v2/product/' + product['offers']['url'].split('/')[-1]).json()
        sold_string = r["status"]
        return sold_string != "ONSALE"
    

#testing
#with open('test.json') as user_file:
#  file_contents = user_file.read()
#  parsed_json = json.loads(file_contents)
#  print(isSold(parsed_json))