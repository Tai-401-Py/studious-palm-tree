import discord, os, datetime
from dotenv import load_dotenv



load_dotenv()

client = discord.Client()
token = os.getenv('TOKEN')

def get_info():

   

@client.event
async def on_ready():
    string = f'Bot has initialized on {datetime.date.today()}'
    print(string.format(client))





@client.event
async def on_message(message):
    print (message)
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Chatter on {channel} > {username} said: {user_message}')

    if message.author == client.user:
        return
 
    if channel == "cividex-development":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')

client.run(token)