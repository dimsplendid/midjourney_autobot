from pathlib import Path

import discord
import logging

from config import bot_token
import user

# load all prompts from prompts.txt file
with open('prompts.txt', 'r') as f:
    prompts = f.readlines()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == 'auto':
            await message.reply('Starting automation, do not type anything in the channel')
            
            user.prompt_to_discord('fantasy word, anime')
        if message.content[-6:] == '(fast)':
            await message.reply('drawing fast complete')
            image_path = Path('images')
            await message.reply(f'downloading image to {image_path}')
            user.download_last_img(image_path, index=2)




intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

if __name__ == '__main__':
    client.run(bot_token, log_handler=handler, log_level=logging.DEBUG)
