import os
import discord
import my_bot
client = discord.Client(intents=discord.Intents.all())
my_secret = os.environ['DISCORD_BOT_SECRET']
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
@client.event
async def on_message(message):
    if message.channel.name == "olivers-bot":
        if message.author != client.user:
            user_name = message.author.display_name
            if my_bot.should_i_respond(message.content, user_name):
                response = my_bot.respond(message.content, user_name)
                await message.channel.send(response)
client.run(my_secret)

