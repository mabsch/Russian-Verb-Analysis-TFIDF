import requests
import csv
import time

def get_category_members(category_title):
    params = {
        'format': 'json',
        'action': 'query',
        'list': 'categorymembers',
        'cmtitle': category_title,
        'cmlimit':128,  # Adjust as needed - 128 shows no issues
    }

    cat_members = []

    start_time = time.time()
    while True:
        resp = requests.get(
            'https://wiktionary.org/w/api.php',
            params=params
        ).json()

        if 'error' in resp:
            raise ValueError(resp['error'])
        if 'warnings' in resp:
            print(resp['warnings'])
        if 'query' in resp:
            data = [(member['title'], member['pageid']) for member in resp['query']['categorymembers']]
            cat_members.append(data)
        if 'continue' not in resp:
            break
        params.update(resp['continue'])
        print(f'Getting next page')

    end_time = time.time()  
    elapsed_time = end_time - start_time
    print(f'Total time taken: {elapsed_time} seconds')

    return cat_members


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'PageID']) 
        for entry in data:
            writer.writerows(entry)

if __name__ == '__main__':
    category_titles = [f'Category: Russian class {i} verbs' for i in range(1,17)] + ['Category: Russian irregular verbs']

    for cat in category_titles:
        cat_members = get_category_members(cat)
        save_to_csv(cat_members, f'{cat.split(":")[-1]}_members.csv')