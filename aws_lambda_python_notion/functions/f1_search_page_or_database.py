import requests


def lambda_handler(event, context):
    try:
        access_token = event['access_token']
        query = event.get('query', '')

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28" 
        }
        params = {
            "query": query
        }
        response = requests.post("https://api.notion.com/v1/search", headers=headers, json=params)
        response_data = response.json()
    except Exception as e:
        response_data = {"error": str(e)}

    return response_data
