import requests

def lambda_handler(event, context):
    try:
        access_token = event['access_token']
        parent_page_id = event['parent_page_id']
        content = event.get('content')

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2021-05-13"
        }
        data = {
            "parent": {
                "page_id": parent_page_id
            },
            "properties": {
                "title": [
                    {
                        "text": {
                            "content": content
                        }
                    }
                ]
            }
        }
        response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
        response_data = response.json()
    except Exception as e:
        response_data = {"error": str(e)}
        
    return response_data

