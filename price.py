  
 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'symbol':'WHX'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0c51e7da-11a2-4eff-a8a9-3c015f35e67b',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
  parseData = json.dumps(response.json())
  #print(parseData)
  ethObj = json.loads(parseData)
  print(ethObj["data"]["WHX"]["name"])
  print(ethObj["data"]["WHX"]["quote"]["USD"]["price"])

  ethString = str(ethObj["data"]["ETH"]["quote"]["USD"]["price"])
  ethPrice = float(ethString)

  if(ethPrice > 0.01):
    print("Whitex To moon")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
