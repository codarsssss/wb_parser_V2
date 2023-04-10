import requests
from settings import ID
from table import save_to_mysql


url = "https://public-feedbacks.wildberries.ru/api/v1/summary/full"

payload = {
    "imtId": ID,
    "take": 30
}
response = requests.request("POST", url, json=payload)

fb_details = response.json()['feedbacks']
data = []
for i in fb_details:
    print(name := i['wbUserDetails']['name'])
    data.append(name)
    print(date := i['createdDate'][:10])
    data.append(name)
    print(text := i['text'])
    data.append(text)
    print(val := i['productValuation'])
    photos = i['photos']
    if photos:
        for j in photos:
            print(j['fullSizeUri'])
            print(j['minSizeUri'])
    print(i['answer']['text'])
    print(i)
    print('---------------------')


