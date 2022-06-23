import discord, os, datetime
from discord.ext import commands
from dotenv import load_dotenv
from helper import Helper


bot = commands.Bot(command_prefix='$')
helper = Helper()

load_dotenv()

token = os.getenv('TOKEN')

  

@bot.event
async def on_ready():
    # string = f'Bot has initialized on {datetime.date.today()}'
    get_fact = helper.request_get()
    string = f"On {get_fact['date']}: {get_fact['fact']}"
    print(string.format(bot))


@bot.event
async def on_message(message):
    '''
    Overides message input and catches text for command operations
    '''
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Chatter on {channel} > {username} said: {user_message}')

    if message.author == bot.user:
        return

    await bot.process_commands(message)
    

@bot.command(name='date')
async def date(ctx):
    '''
    Bot command retrieves dat with $date
    '''
    date_ = f'{datetime.date.today()}'
    await ctx.send(date_)

@bot.command(name ='fact')
async def fact(ctx):
    '''
    Gets and displays random fact
    '''
    get_fact = helper.request_get()
    string = f"On {get_fact['date']}: {get_fact['fact']}"
    await ctx.send(string)


if __name__ == "__main__":
    bot.run(token)
