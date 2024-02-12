import requests
from datetime import datetime



def lambda_handler(event, context):


    access_token = event['access_token']
    database_id = event['database_id']
    properties = event['properties']

    try:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28" 
        }
        data = {
            "parent": {
                "database_id": database_id
            },
            "properties": properties
    }
        response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
        response_data = response.json()
    except Exception as e:
        response_data = {"error": str(e)}

    return response_data

