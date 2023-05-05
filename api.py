import requests
import json

datalist={"merchantNo":"MSN2023042416823040844899JzZXEte","merchantOrderNo":"1682662094","amount":"220","userMobile":"18177777778","sign":"54CA7206FCEA58DDD95F09EFFE56D27C"}

json_data = json.dumps(datalist)
print(json_data)
headers = {'Content-Type': 'application/json'}

r = requests.post("http://api.cloudpayPartner.tyche/api/partner/orders",data=json_data,headers=headers)

print(r.json())

