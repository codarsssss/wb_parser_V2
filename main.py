import os
import shutil
import requests
from settings import ID, TAKE, VALUATION
from save_photos import save_photos
from save_as_CSV import save_csv
from save_as_JSON import save_json


url = "https://public-feedbacks.wildberries.ru/api/v1/summary/full"
payload = {
    "imtId": ID,
    "take": TAKE
}

response = requests.request("POST", url, json=payload)
if response.status_code == 200:
    try:
        if os.name == 'nt':
            os.system('rd /s /q files')
        else:
            os.system('rm -rf files/')

    except OSError as error:
        print(f'Папка не удалена: {error}')
    finally:
        os.mkdir('files/')
else:
    print(f'Ответ от сервера: {response.status_code}')

fb_details = response.json()['feedbacks']

count_id = 1
for i in fb_details:
    name = i['wbUserDetails']['name']
    date = i['createdDate'][:10]
    text = i['text']
    val = i['productValuation']
    photos = i['photos']
    count = 1
    answer = i['answer']['text']
    if val in VALUATION:
        save_csv(count_id, name, date, text, val, answer)
        save_json(count_id, name, date, text, val, answer)
        if photos:
            for j in photos:
                save_photos(count_id, j["fullSizeUri"], count)
                save_photos(count_id, j["minSizeUri"], count, 'min')
                count += 1
        count_id += 1

print('Done')
