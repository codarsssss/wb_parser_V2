import json


def save_json(count_id, name, date, text, val, answer):
    result_json = {count_id: {
        'name': name,
        'date': date,
        'text': text,
        'val': val,
        'answer': answer}}
    with open(f'files/feedback_js.json', 'a', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
