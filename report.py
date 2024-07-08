import requests
import pandas as pd

limit = 100
offset = 0
url = f"https://api.pagerduty.com/extensions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "",
    "Accept": "application/json"
}


def send_request(newurl, headers,limit,offset,verify=False):
    newurl = pagination(limit,offset)
    response = requests.get(newurl, headers=headers, verify=False)
    return response.json()

def pagination(limit,offset):
    return url + f"?limit={limit}&offset={offset}"

def create_list(url,headers,limit,offset):
    datalist = []
    while True:

            r = send_request(url, headers, limit,offset)
            print(f"limit is {limit}")
            print(f"offset is {offset}")
            if len(r['extensions']) == 0:
                break
            for i in r['extensions']:
                data = {
                    "name": i['extension_objects'][0]['summary'],
                    "id": i['id']
                }
                datalist.append(data)
            offset += 100
    df = pd.DataFrame(datalist)
    df.to_csv('extension.csv')
    print(datalist)





create_list(url, headers, 100,0)
