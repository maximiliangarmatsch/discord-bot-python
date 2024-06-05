# Discord Bot Project

## Overview
This project implements a Discord bot using the `discord.py` library. The bot is designed to handle interactions and respond to user commands such as processing email and essay queries. It also logs and forwards user messages to a predefined webhook URL.

## Features
- **Email Command**: Processes email queries and responds with the appropriate output.
- **Essay Command**: Processes essay queries and responds with the appropriate output.
- **Message Handling**: Logs incoming messages and forwards them to a webhook URL.
- **Ready Event**: Synchronizes commands when the bot is ready.

## Setup
```code
conda create env python==3.10
git clone https://github.com/maximiliangarmatsch/discord-bot-python.git
cd discord-bot-python
pip install -r requirements.txt
```
## create .env
```
DISCORD_TOKEN = "Discord Token"
webhook_URL = "MC webhook URL"
gmail_make_api_url = "MC API URL"
make_api_token = "MC API Token"

```
## Run Server

```code
python app.py
```
