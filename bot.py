from pathlib import Path

import discord
import logging

from config import user_id
import user

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # print(f'Message from {message.author}: {message.content}')
        if message.content == 'start' or message.content == 'download complete':
            global prompt_counter
            if prompt_counter < len(prompts):
                await message.reply('Starting automation, do not type anything in the channel')
                prompt = prompts[prompt_counter]
                # prompt += ' --niji 5' # anime style
                user.prompt_to_discord(prompt)
                prompt_counter += 1
            else:
                await message.reply('All prompts are completed, closing the bot')
                print('All prompts are completed, closing the bot')
                await self.close()
            
        if message.content[-6:] == '(fast)':
            await message.reply('drawing fast complete, and start scale up...')
            user.scale_up_img(1)
            
        if message.content[-31:] == f'Image #4 <@{user_id}>':
            await message.reply('scale up complete, and start download...')
            for i in range(4):
                user.download_image(Path('images'), i+1)
            await message.reply('download complete')


if __name__ == '__main__':
    # load all prompts from prompts.txt file
    from config import bot_token
    with open('prompts.txt', 'r') as f:
        prompts = f.readlines()

    prompt_counter = 0
    
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    client.run(bot_token, log_handler=handler, log_level=logging.DEBUG)
