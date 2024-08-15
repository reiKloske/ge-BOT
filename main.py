from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# < Load token from somewhere safe >
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# < Bot Setup >
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# < Message Functionality >
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were prob not enabled)')
        return

    # '?' Is used to private message the user
    is_private = user_message[0] == '?'

    if is_private:
        # The message starts after the '?' ofc
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        # If the message is private '?' send response to Author DM - If NOT private, send on channel.
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# < Handling the startup of the bot >
# Everytime bot goes online we can display in the console so we know that the bot is actually running
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# < Handling incoming messages >
@client.event
async def on_message(message: Message) -> None:
    # If the author of the message is the BOT itself, leave.
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    # Creating logging information
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# < Main Entry Point >
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
