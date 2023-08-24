import requests
import json
import pandas as pd

url1="https://demo.vectra.io/api/v2.2/detections"

df= pd.read_csv("~/Downloads/POC/test.csv")

cmdb=[]
for index,row in df.iterrows():
    cmdb.append(row)
r=requests.get(url1,headers={'Authorization': 'Token <<enter the token>>'})
detections=r.json()
u=detections["results"]
id=[]
for i in u:

    id.append(i["id"])

print(id)
notes=[]
for l in id:
    s=requests.get(f"https://demo.vectra.io/api/v2.5/detections/{l}",headers={'Authorization': 'Token <<enter the token>>'})
    capture = s.json()
    src= capture['src_ip']
    print(src)
    for i in range(len(cmdb)):
        if src == cmdb[i][0]:
            print("yes")
            data=str(cmdb[i])
            print(data)
            x=data.replace("  ","\n")
            x=data.replace("\n","\n \n")
            print(x)
            x = requests.post(f"https://demo.vectra.io/api/v2.5/detections/{l}/notes",
                              headers={'Authorization': 'Token <<enter the token>>',
                                       "Content-Type": "application/json"}, json={"note": x})
            print(x.text)










