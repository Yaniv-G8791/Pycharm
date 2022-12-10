import requests
import json
url = "https://api.apilayer.com/currency_data/convert?base=USD&symbols=EUR,GBP,JPY&amount=5"
payload={}
headers={
    "apikey": "itkpWVg5MbYQLEwGe3RA5bHxg0B1pgWh"

}
res=requests.request("get",url,headers=headers,data=payload)
status_code=res.status_code
result=res.json()
print(res)

#res=requests.get('http://127.0.0.1:30000/data/2')
#if res.ok:
#    print(res.content)
