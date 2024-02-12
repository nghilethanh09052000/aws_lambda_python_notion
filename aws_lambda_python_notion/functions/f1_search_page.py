import requests

def lamda_handler(event, context):

    access_token = 'secret_w3Og6xA7H43GbBZwOYfFwAjNvXlN9YDx4TiIPOlUI0u'

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28" 
    }
    params = {
        "query": 'Notion',
        "filter": {
            "property": "object"
        }
    }
    response = requests.post("https://api.notion.com/v1/search", headers=headers, json=params)

    print('Nghi------------------------', response.json())

    return response.json()

lamda_handler("", "")