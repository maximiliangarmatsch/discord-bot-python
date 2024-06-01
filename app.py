"""
DBS main module
"""
import os
import discord
from typing import Final
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from discord import Intents, Client, Message
import requests

# STEP 0: LOAD OUR TOKEN FROM .env FILE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
webhook_URL = os.getenv("webhook_URL")
intents: Intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

@bot.event
async def on_ready():
    """
    This function is called automatically when the bot has successfully logged in
    and is ready to start interacting with the Discord API.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    print("Bot is ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(str(e))

@bot.tree.command(name="email")
@app_commands.describe(query="Type email description here")
async def email(interaction: discord.Interaction, query: str):
    """
    This command takes an email query, processes it, and sends a response back to the user..

    Parameters
    ----------
    interaction : discord.Interaction
        The interaction object that represents the command invocation context.
    query : str
        user input or query.

    Returns
    -------
    None
    """
    await interaction.response.defer()
    try:
        response = "Hard Code Response For Email Query"
        await interaction.followup.send(f"{response}")
    except discord.errors.NotFound as e:
        print(f"Interaction error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@bot.tree.command(name="count")
@app_commands.describe(query="Type essay description here")
async def count(interaction: discord.Interaction, query: str):
    """
    This command takes an count query, processes it, and sends a response back to the user.

    Parameters
    ----------
    interaction : discord.Interaction
        The interaction object that represents the command invocation context.
    query : str
        user query or input.

    Returns
    -------
    None
    """
    await interaction.response.defer()
    try:
        response = "Hard Code Response For Count"
        await interaction.followup.send(f"{response}")
    except discord.errors.NotFound as e:
        print(f"Interaction error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@bot.tree.command(name="essay")
@app_commands.describe(query="Type essay description here")
async def essay(interaction: discord.Interaction, query: str):
    """
    This command takes an essay query, processes it, and sends a response back to the user.

    Parameters
    ----------
    interaction : discord.Interaction
        The interaction object that represents the command invocation context.
    query : str
        user query or input.

    Returns
    -------
    None
    """
    await interaction.response.defer()
    try:
        response = "Hard Code Response For Essay"
        await interaction.followup.send(f"{response}")
    except discord.errors.NotFound as e:
        print(f"Interaction error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    """
    This function sends a user message to a predefined webhook URL.

    Parameters
    ----------
    message : Message
        The message object containing details about the message context.
    user_message : str
        User query or input.

    Returns
    -------
    None
    """
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    # if is_private := user_message[0] == '?':
    #     user_message = user_message[1:]
    try:
        requests.post(f"{webhook_URL}message={user_message}")
    except Exception as e:
        print(e)

# STEP 4: HANDLING INCOMING MESSAGES
@bot.event
async def on_message(message: Message) -> None:
    """
    This function is called automatically whenever a message is sent in a channel
    that the bot has access.

    Parameters
    ----------
    message : Message
        The message object representing the incoming message.

    Returns
    -------
    None
    """
    if message.author == bot.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# STEP 5: MAIN ENTRY POINT
def main() -> None:
    """
    This function initializes and runs the Discord bot using the provided token.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bot.run(token=TOKEN)


if __name__ == '__main__':
    main()
