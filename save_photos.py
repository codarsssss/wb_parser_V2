import os
import requests


def save_photos(count_id, link, number, size='full'):

    dir_name = f'{count_id}'
    res = requests.get(url=f'https://feedbackphotos.wbstatic.net/{link}')
    if os.path.isdir(f'files/{dir_name}'):
        with open(f'files/{dir_name}/{number}_{size}.jpeg', 'wb') as file:
            file.write(res.content)
    else:
        os.mkdir(f'files/{dir_name}')
        with open(f'files/{dir_name}/{number}_{size}.jpeg', 'wb') as file:
            file.write(res.content)
