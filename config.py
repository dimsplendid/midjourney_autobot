import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
if bot_token is None:
    raise ValueError('BOT_TOKEN environment variable not found')
else:
    bot_token = bot_token # just for type hint purposes

server_id = os.getenv('SERVER_ID')
if server_id is None:
    raise ValueError('SERVER_ID environment variable not found')
else:
    server_id = server_id # just for type hint purposes
    
channel_id = os.getenv('CHANNEL_ID')
if channel_id is None:
    raise ValueError('CHANNEL_ID environment variable not found')
else:
    channel_id = channel_id # just for type hint purposes

discord_token = os.getenv('DISCORD_TOKEN')
if discord_token is None:
    raise ValueError('DISCORD_TOKEN environment variable not found')
else:
    discord_token = discord_token # just for type hint purposes
    
user_id = os.getenv('USER_ID')
if user_id is None:
    raise ValueError('USER_ID environment variable not found')
else:
    user_id = user_id