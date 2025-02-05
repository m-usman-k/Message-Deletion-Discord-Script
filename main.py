import requests, time, re

AUTHORIZATION = ""
CHANNEL_ID = 982628207402577920
URL_PATTERN = re.compile(r"https?://\S+")


def get_first_100_messages() -> list:
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit=100"
    headers = {
        "Authorization": AUTHORIZATION
    }
    
    response = requests.get(url, headers=headers)
    return response.json()
    
    
def get_messages_before_id(id: int) -> list:
    ...
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?before={id}&limit=100"
    headers = {
        "Authorization": AUTHORIZATION
    }
    
    response = requests.get(url, headers=headers)
    return response.json()

def delete_message(id: int):
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages/{id}"
    headers = {
        "Authorization": AUTHORIZATION
    }
    
    response = requests.delete(url, headers=headers)
    print(response.status_code)
    
def main():
    messages = get_first_100_messages()
    for message in messages:
        if URL_PATTERN.search(message['content']):  # Check if the message contains a URL
            print(f"Deleting message {message['id']}")
            delete_message(message['id'])
            time.sleep(2)
        
    while True:
        messages = get_messages_before_id(messages[-1]['id'])
        if not messages:
            break
        for message in messages:
            if URL_PATTERN.search(message['content']):  # Check if the message contains a URL
                print(f"Deleting message {message['id']}")
                delete_message(message['id'])
                time.sleep(2)
            
    print("Done!")
    
    
if __name__ == "__main__":
    main()