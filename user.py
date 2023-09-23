import os
import requests
from pathlib import Path

import time

from config import discord_token, server_id, channel_id

# convenient json variable aliases
true = True
false = False
null = None

def prompt_to_discord(prompt):
    headers = {
        'Authorization': discord_token,
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0'
    }
    
    # Check the payload format by sending a request to the discord API
    # res = requests.get(
    #     f'https://discord.com/api/v10/channels/{channel_id}/application-commands/search?type=1&include_applications=true&query=imagine',
    #     headers = headers
    # )
    # print(res)
    # print(res.content)
    
    payload = {
        "type": 2,
        "application_id": "936929561302675456",
        "guild_id": server_id,
        "channel_id": channel_id,
        "session_id": 12343,
        "data": {
            "version": "1118961510123847772",
            "id": "938956540159881230",
            "name": "imagine",
            "type": 1,
            "options": [
                {
                    "type": 3,
                    "name": "prompt",
                    "value": prompt
                }
            ],
            "application_commands": [
                {
                    "id": "938956540159881230",
                    "application_id": "936929561302675456",
                    "version": "1118961510123847772",
                    "default_member_permissions": null,
                    "type": 1,
                    "nsfw": false,
                    "name": "imagine",
                    "description": "Create images with Midjourney",
                    "dm_permission": true,
                    "contexts": [
                        0,
                        1,
                        2
                    ],
                    "integration_types": [
                        0
                    ],
                    "options": [
                        {
                            "type": 3,
                            "name": "prompt",
                            "description": "The prompt to imagine",
                            "required": true
                        }
                    ]
                }
            ],
            "attachments": []
        }
    }
    
    response = requests.post(
        'https://discord.com/api/v10/interactions', 
        headers=headers, 
        json=payload
    )
    
    return response

def get_messages():
    headers = {
        'Authorization': discord_token,
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0'
    }
    
    response = requests.get(
        f'https://discord.com/api/v10/channels/{channel_id}/messages', 
        headers=headers
    )
    
    return response

def download_image(path: Path, index=0):
    res = get_messages()
    json_data = res.json()
    img_url = json_data[index]["attachments"][0]["url"]
    img_name = json_data[index]["attachments"][0]["filename"]
    img = requests.get(img_url).content
    with open(path / img_name, 'wb') as f:
        f.write(img)
        
def scale_up_img(message_index = 0):
    headers = {
        'Authorization': discord_token,
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0'
    }
    
    messages = get_messages().json()
    message_id = messages[message_index]["id"]
    
    for i in range(4): 
        component = messages[message_index]["components"][0]["components"][i]
        custom_id = component["custom_id"]
        payload = {
            "type": 3,
            "guild_id": server_id,
            "channel_id": channel_id,
            "message_flags": 0,
            "message_id": message_id,
            "application_id": "936929561302675456",
            "session_id": 12345,
            "data": {
                "component_type": 2,
                "custom_id": custom_id
            }
        }
        
        response = requests.post(
            'https://discord.com/api/v10/interactions', 
            headers=headers, 
            json=payload
        )
        # print(response)
        time.sleep(1)                      

if __name__ == '__main__':
    # using for testing
    import simplejson as json
    
    res = get_messages()
    json_data = res.json()
    
    with open('discord.json', 'w') as f:
        json.dump(json_data, f, indent=4)
