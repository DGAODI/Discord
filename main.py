# This example requires the 'message_content' intent.

import discord
import me_def

import os


intents = discord.Intents.default()

client = discord.Client(intents=intents)


command_list = '''!hello - приветствие
!fox - рандомное фото лисы
!анекдот - ну тут сам понимаешь'''



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    author = message.author
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello, {author.mention}!')
    if message.content.startswith('!fox'):
        fox = me_def.get_fox()
        await message.channel.send(fox)
    if message.content.startswith('!анекдот'):
        anekdot = me_def.get_anekdot()
        await message.channel.send(anekdot)
    if message.content.startswith('!help'):
        await message.channel.send(command_list)



client.run('MTAwNjQ5OTAyOTA2NjE5OTA0MA.Gxr3cF.ws2ngC1qQZOfTT0FHhsHKczjPKpyXFJe7chm0w')





