# Auto Midjourney

## Description

This is a simple script to automate the process of midjourney. This using the bot to read the prompts and downloads all images all in once.

## Setup

1. Create a virtual environment with conda

```bash
conda create -n midjourney_test python=3.11
```

2. Activate the virtual environment

```bash
conda activate midjourney_test
```

3. Install the requirements

```bash
pip install -r requirements.txt
```

4. Create a .env file with the following variables

```bash
BOT_TOKEN=your_bot_token
DISCORD_TOKEN=your_discord_token
CHANNEL_ID=your_channel_id
SERVER_ID=your_server_id
USER_ID=your_user_id
```

5. Create an `images` foler in the root directory

## Usage

1. Modify the `prompts.txt` file with your own prompts
2. Run the script

```bash
python bot.py
```
3. In the chat room, type `start` to start auto midjourney:D
