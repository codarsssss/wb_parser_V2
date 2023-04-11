import os
import csv


def save_csv(count_id, name, date, text, val, answer):
    if not os.path.isfile(f'files/feedback_table.csv'):
        with open(f'files/feedback_table.csv', 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['id', 'Name', 'Date', 'Text', 'Valuation', 'Answer'])

    with open(f'files/feedback_table.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([count_id, name, date, text, val, answer])
